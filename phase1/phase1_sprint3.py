from functools import partial
from collections.abc import Callable
from phase1_sprint2 import compose
# from itertools import chain


def power_of(x: int, y: int) -> int:
    return pow(x, y)


square = partial(power_of, y=2)


def my_partial(func: Callable, *preset_args, **preset_kwargs) -> Callable:
    def wrapper(*args, **new_kwargs):
        seq_tupl = preset_args + args
        merged_kwargs = {**preset_kwargs, **new_kwargs}

        return func(*seq_tupl, **merged_kwargs)

    return wrapper


my_square = my_partial(power_of, y=2)


def chain_two(a: list, b: list):
    result = []

    for x in a:
        result.append(x)

    for y in b:
        result.append(y)

    return result


def longer_than(word: str, threshold: int) -> bool:
    return len(word) > threshold


is_long = my_partial(longer_than, threshold=5)


def take_two(string: str) -> str:
    return string[:2]


first_upper = compose(str.upper, take_two)

if __name__ == "__main__":
    assert square(5) == 25, f"sqaure partial defined incorrectly expecting 25, but returned {square(5)} instead"

    assert my_square(7) == square(7), f"expecting {True} because 49 == 49"
    assert my_square(10) == square(10), f"expecting {True} because 100 == 100"

    assert chain_two([1, 2], [3, 4]) == [1, 2, 3, 4], "the boolean equivalency check does not hold"
    assert chain_two([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8], "the boolean equivalency check does not hold"
    assert chain_two(list(range(0, 5)), list(range(5, 10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "the boolean equivalency check does not hold"
    assert chain_two([], []) == []

    list_a = ["apple", "Banana"]
    list_b = ["cherry", "Date"]

    words = ["apple", "Banana", "cherry", "Date"]

    combined = chain_two(list_a, list_b)

    result = []

    for w in combined:
        if is_long(w):
            result.append(first_upper(w))
        else:
            continue

    assert first_upper("Banana") == "BA"
    assert first_upper("Cherry") == "CH"

    expected = ["BA", "CH"]
    assert result == expected, f"Got {result}, expected {expected}"

# understanding closures better now, partials was not as straight forward though
# understanding how iteration works under the hood

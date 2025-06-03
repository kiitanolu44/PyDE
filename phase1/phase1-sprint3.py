from functools import partial
from collections.abc import Callable
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

my_square = my_partial(pow, exp=2)

def chain_two(a: list, b: list):
    for x in a:
        for y in x:
            yield [x, y]
    



if __name__ == "__main__":
    assert square(5) == 25, f"sqaure partial defined incorrectly expecting 25, but returned {square(5)} instead"

    assert my_square(7) == square(7), f"expecting {True} because 49 == 49"
    assert my_square(10) == square(10), f"expecting {True} because 100 == 100"


    lising = list(range(0, 5))
    lister = list(range(5, 10))

    work = chain_two(lising, lister)
    print(work)
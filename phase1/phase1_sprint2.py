from time import perf_counter_ns
from collections.abc import Callable
from functools import wraps

# cache = {}

# def memo_fib(n: int) -> dict[int]:
#     if n in cache:
#         return cache[n]
#     else:
#         fibonacci(n)
#         cache[n] = fibonacci(n)
#         return cache[n]


def memoize(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict):
        key = args + (tuple(sorted(kwargs.items())))

        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def f(x: int) -> int:
    return x + 1


def g(x: int) -> int:
    return x * 2


def compose(f: Callable, g: Callable) -> Callable:
    def inner(x: int) -> int:
        result = g(x)
        final_result = f(result)
        return final_result

    return inner


nums = range(20)

result_list = []

for x in nums:
    y = x * 2

    if y % 3 == 0:
        result_list.append(y)

expected = [0, 6, 12, 18, 24, 30, 36]

if __name__ == "__main__":
    start = perf_counter_ns()
    result = fibonacci(30)
    stop = perf_counter_ns()
    duration_ms = (stop - start) / 1_000_000

    assert result == 832040
    assert duration_ms < 50, f"expected less than 50 ms but got {duration_ms:.2f} ms"

    print(f"fibonacci(30) took {duration_ms:.2f} ms")

    t1_start = perf_counter_ns()
    fibonacci(30)
    t1_stop = perf_counter_ns()

    first_run = t1_stop - t1_start

    t2_start = perf_counter_ns()
    fibonacci(30)
    t2_stop = perf_counter_ns()

    second_run = t2_stop - t2_start

    assert second_run < (first_run * 0.5), f"expected >= 50% speedup but got {second_run:.2f}/{first_run:.2f}"

    print(f"first run: {first_run} second run: {second_run}")

    h = compose(f, g)

    assert h(4) == f(g(4)), f"your function composition {compose} has not bee defined correctly"
    assert h(10) == f(g(10)), f"your function composition {compose} has not bee defined correctly"

    print(f"h(4) is equal to {h(4)}, which is defined correctly as being equal to f(g(4)) ({f(g(4))})")

    assert result_list == expected, f"there has been an error in manual map/filter: got {result_list}, expected {expected}"

# it was repititve to do the perf counter everytime, maybe if i could set it so that any time i ran a function it would tell me how long it takes that would be good

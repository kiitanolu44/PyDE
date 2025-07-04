import sys
from collections.abc import Callable
import logging
from functools import wraps

from functools import lru_cache
from time import perf_counter_ns

from utils.PyDE_utils import setup_logging

logger = logging.getLogger(__name__)


def gen_squares_div4(val: int):
    for i in range(val):
        if i % 4 == 0:
            yield i**2


def log_calls(func: Callable) -> None:
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Calling...")
        return func(*args, **kwargs)

    return wrapper


@log_calls
def greet(name):
    """say hello"""
    return f"Hi {name}"


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("running script")
    gen_exp = (i**2 for i in range(20) if i % 4 == 0)
    assert next(gen_exp) == 0
    assert next(gen_exp) == 16
    assert next(gen_exp) == 64

    gen_exp = (i**2 for i in range(20) if i % 4 == 0)
    assert list(gen_exp) == [0, 16, 64, 144, 256]

    assert list(gen_squares_div4(20)) == [0, 16, 64, 144, 256]

    gen_exp = (i**2 for i in range(20) if i % 4 == 0)
    assert list(gen_squares_div4(20)) == list(gen_exp)

    assert greet.__name__ == "greet"
    assert greet.__doc__ == "say hello"

    fib_1_start = perf_counter_ns()
    fibonacci(30)
    fib_1_stop = perf_counter_ns()

    fib_1_duration = fib_1_stop - fib_1_start

    fib_2_start = perf_counter_ns()
    fibonacci(30)
    fib_2_stop = perf_counter_ns()

    fib_2_duration = fib_2_stop - fib_2_start

    logger.info("fib 1 call is %d nanoseconds, fib 2 call is %d nanoseconds", fib_1_duration, fib_2_duration)

    assert fib_2_duration < 0.1 * fib_1_duration


if __name__ == "__main__":
    sys.exit(main())

# wraps allowed me to access the nested function's information
# lru cache sped up my fib call by more than 90%

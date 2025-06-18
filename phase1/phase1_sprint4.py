import sys
from collections.abc import Callable
import logging
from logging import Logger
from functools import wraps
from phase1_sprint2 import memoize
from functools import lru_cache

from PyDE_utils import setup_logging

logger = logging.getLogger(__name__)

def gen_squares_div4(val: int):
    for i in range(val):
        if i % 4 == 0:
            yield i**2


def log_calls(func: Callable) -> None:
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Calling...")
        func()

    return wrapper


@log_calls
def greet(name):
    """say hello"""
    return f"Hi {name}"

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

if "__main__" == __name__:
    sys.exit(main())

import sys
import my_module
from pkg import foo, bar, bar_check

import importlib


def main() -> None:
    assert my_module.WAS_CALLED == False

    assert foo() == "A"
    assert bar() == "B"

    assert bar_check() == "A-B"

    name = "pkg.a"
    mod = importlib.import_module(name)
    result = mod.foo()

    assert result == "A"


if __name__ == "__main__":
    sys.exit(main())


# absolute imports feel the most intuitive to me, but i can see how relative imports can be useful

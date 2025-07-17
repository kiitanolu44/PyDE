from .a import foo


def bar() -> str:
    return "B"


def bar_check() -> str:
    return foo() + "-B"

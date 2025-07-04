import sys

WAS_CALLED = False


def hello() -> None:
    global WAS_CALLED
    WAS_CALLED = True
    print("Hello, Modules!")


def main() -> None:
    hello()


if __name__ == "__main__":
    sys.exit(main())

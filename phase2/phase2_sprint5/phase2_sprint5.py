import sys
import pathlib
import os
import importlib.resources


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    sprint4 = script_path.parent.parent / "phase2_sprint4"
    sys.path.insert(0, str(sprint4))

    # 1

    text_import = importlib.resources.files("pkg").joinpath("data", "greeting.txt")
    text = text_import.read_text(encoding="utf-8")

    # assert importlib.resources.files("pkg.data").joinpath("greeting.txt") == "Hello, Data!"

    assert text.strip() == "Hello, Data!"

    # 2

    import pkg  # type: ignore

    assert pkg.__version__ == "0.1.0"

    # 3

    os.environ["USE_FAST"] = "0"

    if os.environ.get("USE_FAST") == "1":
        from fast_impl import work
    else:
        from safe_impl import work

    assert work() == "safe"

    os.environ["USE_FAST"] = "1"

    if os.environ.get("USE_FAST") == "1":
        from fast_impl import work
    else:
        from safe_impl import work

    assert work() == "fast"

    # 4

    assert sys.prefix != sys.base_prefix, "The venv is not active"


if __name__ == "__main__":
    sys.exit(main())

# the work with os.environ made me actually understand how powerful docker is, especially when trying to ensure standardisation across different working environments

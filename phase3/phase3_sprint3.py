import os
import sys
import io
import logging

class PipelineError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
class DataError(PipelineError):
    def __init__(self, *args):
        super().__init__(*args)

class ConfigError(PipelineError):
    def __init__(self, *args):
        super().__init__(*args)

def process(data: dict) -> None:
    if isinstance(data, dict) and "value" in data.keys():
        return
    else:
        raise DataError("not a dict")
    
def buggy(n: int) -> float:
    return 1/(n-1)

def divide(a, b) -> float:
    assert b != 0
    return a / b

def divide_safe(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b

def main() -> None:

    # 1 

    phase3 = logging.getLogger(__name__)
    phase3.setLevel(logging.DEBUG)

    
    console_capture = io.StringIO()

    if not phase3.handlers:
        console_handler = logging.StreamHandler(console_capture)
        file_handler = logging.FileHandler("phase3.log", mode="a", encoding="utf-8")

        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        phase3.addHandler(console_handler)
        phase3.addHandler(file_handler)

        phase3.debug("i am hungry")
        phase3.info("any one want to feed me?")

        for h in phase3.handlers:
            if hasattr(h, "flush"):
                h.flush()


    console_contents = console_capture.getvalue()

    assert "any one want to feed me?" in console_contents
    assert "i am hungry" not in console_contents

    with open("phase3.log", "r") as file:
        lines = file.readlines()
        assert any("i am hungry" in line for line in lines)
        assert any("any one want to feed me?" in line for line in lines)
    
    if os.path.exists("phase3.log"):
        os.remove("phase3.log")

    for h in phase3.handlers:
        h.close()
    phase3.handlers.clear()



    # 2

    try:
        process({})
    except PipelineError as e:
        assert isinstance(e, DataError)

    # 3
    
    try:
        buggy(1)
    except ZeroDivisionError as e:
        import pdb
        if os.getenv("PYDE_POST_MORTEM", "0") == "1":
            pdb.post_mortem(e.__traceback__)
        else:
            print("ZeroDivisionError caught; set PYDE_POST_MORTEM=1 to drop into pdb post-mortem.")


    
    # 4

    try:
        divide(10, 0)
    except Exception as e:
        assert isinstance(e, AssertionError)

    try:
        divide_safe(10, 0)
    except Exception as e:
        assert isinstance(e, ValueError)
    
if __name__ == "__main__":
    sys.exit(main())
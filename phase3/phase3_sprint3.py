import os
import sys
import io
import logging

def main() -> None:

    # 1 

    phase3 = logging.getLogger(__name__)
    phase3.setLevel(logging.DEBUG)

    console_capture = io.StringIO()
    console_handler = logging.StreamHandler(console_capture)
    

    file_handler = logging.FileHandler("phase3.log", mode="a", encoding="utf-8")

    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    
    phase3.addHandler(console_handler)
    phase3.addHandler(file_handler)

    phase3.info("this is my info message")
    phase3.debug("this is my debug message")

    console_contents = console_capture.getvalue()

    assert "this is my info message" in console_contents
    assert "this is my debug message" not in console_contents

    with open("phase3.log", "r") as file:
        lines = file.readlines()
        assert any("this is my info message" in line for line in lines)
        assert any("this is my debug message" in line for line in lines)
    
    if os.path.exists("phase3.log"):
        os.remove("phase3.log")

if __name__ == "__main__":
    sys.exit(main())
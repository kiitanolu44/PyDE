import subprocess
import pathlib
import sys
from zipfile import ZipFile


def main() -> None:
    with ZipFile("/Users/kiitanoluwasere/Documents/Data Engineering/git/PyDE/phase2/phase2_sprint4/dist", "r") as zip:
        zip_list = zip.namelist()

        assert "pkg/__init__.py" in zip_list

if __name__ == "__main__":
    sys.exit(main())
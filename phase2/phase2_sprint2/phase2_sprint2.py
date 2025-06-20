# from pkg import *
import sys
from PyDE_utils import setup_logging
import phase2.phase2_sprint1.pkg.a as m
import logging


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.debug("task 1 & 2")
    assert m.__name__ == "phase2.phase2_sprint1.pkg.a"
    assert ".py" in m.__file__
    assert m.__package__ == "phase2.phase2_sprint1.pkg"


    

if __name__ == "__main__":
    sys.exit(main())
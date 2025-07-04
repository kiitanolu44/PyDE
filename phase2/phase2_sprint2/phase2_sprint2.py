from pkg import *  # noqa: F403
import sys
from PyDE_utils import setup_logging
import phase2.phase2_sprint1.pkg.a as m
import logging
import pkgutil
import plugins

import os
import runpy


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    assert "foo" in globals()
    assert "bar" not in globals()
    assert "baz" not in globals()

    assert m.__name__ == "phase2.phase2_sprint1.pkg.a"
    assert ".py" in m.__file__
    assert m.__package__ == "phase2.phase2_sprint1.pkg"

    file = "temp_mod.py"
    base = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, base)

    with open(file, "w") as f:
        f.write("def func() -> None:\n    return 'v1'\n")

    module_ns = runpy.run_path(file, run_name="temp_mod")
    assert module_ns["func"]() == "v1"

    with open(file, "w") as f:
        f.write("def func() -> None:\n    return 'v2'\n")

    module_ns = runpy.run_path(file, run_name="temp_mod")
    assert module_ns["func"]() == "v2"

    package = plugins
    prefix = package.__name__ + "."
    module_list = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix=prefix):
        logger.info("found submodule %s (is a package: %s)", modname, ispkg)
        module = __import__(modname, fromlist="dummy")
        module_list.append(modname)
        logger.info("Imported: %s", module)

    logger.info("list of vars in module list: %s", module_list)

    assert module_list == ["plugins.p1_plugin", "plugins.p2_plugin"]


if __name__ == "__main__":
    sys.exit(main())

# this sprint required me to be a little bit more creative than i had been before, understanding how python imports at a deeper level was fun though

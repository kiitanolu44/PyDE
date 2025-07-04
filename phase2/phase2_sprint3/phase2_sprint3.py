import importlib
import importlib.abc
import importlib.metadata
import importlib.util
from importlib.machinery import PathFinder
import sys
import zipimport

def main() -> None:
    # 1
    spec1 = PathFinder.find_spec("mod", path=["/Users/kiitanoluwasere/Documents/Data Engineering/git/PyDE/phase2/phase2_sprint3/part1/ns_pkg"])
    mod1 = importlib.util.module_from_spec(spec1)
    spec1.loader.exec_module(mod1)

    spec2 = PathFinder.find_spec("mod", path=["/Users/kiitanoluwasere/Documents/Data Engineering/git/PyDE/phase2/phase2_sprint3/part2/ns_pkg"])
    mod2 = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(mod2)


    assert mod1.ORIGIN == "part1"
    assert mod2.ORIGIN == "part2"

    # 2

    dists = importlib.metadata.distributions(path=["/Users/kiitanoluwasere/Documents/Data Engineering/git/PyDE/phase2/phase2_sprint3"])

    greet_ep = None

    for dist in dists:
        for ep in dist.entry_points:
            if ep.group == "console_scripts" and ep.name == "greet":
                greet_ep = ep

    func = greet_ep.load()

    assert func() == "Hello CLI"


    # 3

    zip_loader = zipimport.zipimporter("bundle.zip")

    # load_module method due to be deprecated so to future proof i pivoted to exec_module
    # zmod = zipimport.zipimporter.load_module("zmod")

    zip_spec = importlib.util.spec_from_loader("zmod", zip_loader)

    zmodule = importlib.util.module_from_spec(zip_spec)
    
    zip_spec.loader.exec_module(zmodule)

    assert zmodule.VALUE == 123
    assert "bundle.zip" in zmodule.__file__, "Module wasn’t loaded from the ZIP"


    # 4



    

if __name__ == "__main__":
    sys.exit(main())

"""
phase2/phase2_sprint3/
├── part1_root/
│   └── ns_pkg/
│       └── mod.py
├── part2_root/
│   └── ns_pkg/
│       └── mod.py
├── cli.py             ← defines your `main()` function
├── setup.py           ← declares the `greet=cli:main` console_script entry point
└── phase2_sprint3.py  ← your sprint script that will:
                       • write/overwrite cli.py & setup.py
                       • call importlib.metadata.entry_points()
                       • load “greet” and invoke it
                       • assert it returns "Hello CLI"
"""
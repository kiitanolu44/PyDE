import importlib.abc
import importlib.metadata
import importlib.util
from importlib.machinery import PathFinder
import sys
import zipimport


class HookLoader(importlib.abc.Loader):
    def exec_module(self, module):
        module.X = 999


class HookFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname != "hook_mod":
            return None

        return importlib.util.spec_from_loader("hook_mod", HookLoader())


sys.meta_path.insert(0, HookFinder())


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
    import hook_mod  # type: ignore

    assert hook_mod.X == 999, "Custom import hook failed to set X correctly"


if __name__ == "__main__":
    sys.exit(main())

# reflection
# wow this sprint was really a struggle for me, it spanned dynamic imports module systems and even basic api design
# i can see myself using what i learned here in data pipelines where i might need to leverage variable imports from modules that might change dynamically
# it was a great learning experience but blimey im happy to move on!

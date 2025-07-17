import subprocess
import pathlib
import sys

from zipfile import ZipFile


script_path = pathlib.Path(__file__).resolve()
project_root = script_path.parent
project_root_str = str(project_root)


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            "dist",
        ],
        cwd=project_root_str,
        check=True,
    )

    # 1

    wheel_files = list((project_root / "dist").glob("pkg_test-*.whl"))

    with ZipFile(wheel_files[0], "r") as zip:
        zip_list = zip.namelist()

    assert "pkg/__init__.py" in zip_list

    # 2 & 3

    sys.path.insert(0, str(project_root))

    from pkg.a import foo

    assert foo() == "A"

    # used this to discover my package
    # dists = list(importlib.metadata.distributions())

    # for dist in dists:
    #     print(" -", dist.metadata["Name"], dist.version)

    # from importlib.metadata import distributions

    # dist_dir = os.path.join(project_root, "dist")

    # found_version = None
    # for dist in distributions(path=[dist_dir]):
    #     if dist.metadata["Name"] == "pkg-test":
    #         found_version = dist.version
    #         break

    # assert found_version == "0.1.0"

    from importlib.metadata import version

    assert version("pkg-test") == "0.1.0"

    # 4

    from importlib.metadata import entry_points

    plugins = entry_points(group="pyde.plugins")

    for ep in plugins:
        if ep.name == "echo":
            func = ep.load()
            break
    else:
        raise RuntimeError("echo entry point not found")

    assert func() == "A"


if __name__ == "__main__":
    sys.exit(main())

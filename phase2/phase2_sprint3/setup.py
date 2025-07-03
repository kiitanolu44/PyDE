from setuptools import setup

setup(
    name="package44",
    version="0.1.1",
    py_modules=["cli"],
    entry_points={
        "console_scripts": ["greet=cli:main"]
}
)

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("hello._hello", ["hello/_hello.pyx"])
]

setup(
    name = "Hello world!",
    version = 1.0,
    ext_modules = ext_modules,
    packages = ["hello"],
)

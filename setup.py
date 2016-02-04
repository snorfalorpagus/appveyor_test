from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("hello", ["hello.pyx"])
]

setup(
  name = 'Hello world app',
  ext_modules = ext_modules,
)

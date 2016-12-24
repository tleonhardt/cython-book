from setuptools import setup
from Cython.Build import cythonize
setup(
    name="mycodepy",
    ext_modules=cythonize('mycodepy.pyx'),
)

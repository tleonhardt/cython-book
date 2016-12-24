from setuptools import setup
from Cython.Build import cythonize

setup(
    name = 'helloworld',
    ext_modules = cythonize('helloworld.pyx', compiler_directives={'embedsignature': True}),
)

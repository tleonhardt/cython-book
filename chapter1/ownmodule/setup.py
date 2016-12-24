from setuptools import setup, Extension
from Cython.Build import cythonize

sourcefiles = ['PyAddFunction.pyx', 'AddFunction.c']

extensions = [Extension("PyAddFunction", sourcefiles)]

setup(
    name = 'PyAddFunction',
    ext_modules = cythonize(extensions, compiler_directives={'embedsignature': True}),
)

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'PyAddFunction',
    ext_modules = cythonize('PyAddFunction.pyx', compiler_directives={'embedsignature': True}),
)

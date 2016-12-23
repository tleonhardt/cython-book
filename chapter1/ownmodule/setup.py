from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['PyAddFunction.pyx', 'AddFunction.c']

extensions = [Extension("PyAddFunction", sourcefiles)]

setup(
    name = 'PyAddFunction',
    ext_modules = cythonize(extensions, compiler_directives={'embedsignature': True}),
)

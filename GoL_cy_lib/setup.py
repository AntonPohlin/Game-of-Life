from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("*.pyx"))


# cmd: "python setup.py build_ext --inplace"!!

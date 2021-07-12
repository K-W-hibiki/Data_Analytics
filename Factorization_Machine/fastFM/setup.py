#from distutils.core import setup, Extension
#rom Cython.Build import cythonize
#from numpy import get_include # cimport numpy を使うため

#ext = Extension("ffm", sources=["ffm.pyx"], include_dirs=['.', get_include()])
#setup(name="ffm", ext_modules=cythonize([ext]))

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("ffm", ["ffm.pyx"])]
)
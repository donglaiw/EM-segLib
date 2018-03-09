from Cython.Distutils import build_ext
from setuptools import setup, Extension 
import numpy as np

def getExt():
    # extensions under segmenation/
    return [
        Extension(
            name='segLib.dist',
            sources=['segLib/dist.pyx'],
            extra_compile_args=['-O4', '-std=c++0x'],
            language='c++'
        ),
        Extension(
            name='segLib.seg',
            sources=['segLib/seg.pyx'],
            extra_compile_args=['-O4', '-std=c++0x'],
            language='c++'
        ),
        Extension(
            name='segLib.eval',
            sources=['segLib/eval.pyx'],
            extra_compile_args=['-O4', '-std=c++0x'],
            language='c++'
        )
    ]

if __name__=='__main__':
    # python setup.py develop install
    setup(name='segLib',
       version='1.0',
       cmdclass = {'build_ext': build_ext}, 
       include_dirs=[np.get_include()], 
       packages=['segLib'],
       ext_modules = getExt())



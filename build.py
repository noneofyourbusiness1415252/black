from Cython.Build import cythonize

def build(setup_kwargs):
    setup_kwargs.update({'ext_modules':  cythonize(["black.py"])})
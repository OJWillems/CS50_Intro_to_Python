# PyPI stands for Python Package Index
# pip is a package manager that comes with Python that allows you to install packages on your environment
# In your terminal, type: 'pip install cowsay'

import cowsay # type: ignore
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"hello {sys.argv[1]}")
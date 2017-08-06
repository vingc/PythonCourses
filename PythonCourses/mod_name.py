#! python
import sys

print("mod_name.py name:", __name__ ) #main means runs by itself
import pythonenv

print("mod_name.py name:", __name__ ) #main means runs by itself

import docStringFunc

print("call by mod_name:")
docStringFunc.printMax(3,4)

a =2
def xs():
    pass

del a,xs #del names
print(dir())

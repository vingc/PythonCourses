#! python

import sys  #from sys import *  or from sys import argv
import os

print("pythonenv.py name:", __name__ ) #main means runs by itself
__name__="sss"
print("pythonenv.py name:", __name__ ) #main means runs by itself

print("Here is arguments:\n")
cnt = 0
for i in sys.argv:
    print( cnt, i )
    cnt+=1
    
print("\n\nHere is path:\n")
cnt = 0;
for i in sys.path:
    print(cnt, i)
    cnt+=1

print("current directory:",os.getcwd())

#!/usr/bin/python
# Filename: using_file.py



poem = '''\
Programming is fun
When the work is done
   use python.'''

f = open("poem.txt", 'w')
f.write(poem)
f.close()

f = open("poem.txt")

while True:
    line = f.readline()
    if len(line) == 0: #EOF
        break;
    print(line, end='')

f.close()
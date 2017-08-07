#! python
# Filename: try_except.py

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt as ex: #ex is the object of exception type
    print('You cancelled the operation.', ex)
else:
    print('You entered {0}'.format(text))
    for line in f:
        print(line,end='')
#! python
# Filename: try_except.py

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt as ex: #ex is the object of exception type
    print('You cancelled the operation.', ex)
else:
    print('You entered {0}'.format(text))finally:    print("finally")with open("poem.txt") as f:
    for line in f:
        print(line,end='')#use define exception, like javaclass UserInputException(Exception):    def __init__(self, name):        Exception.__init__(self)        self.name = nametry:    raise UserInputException("rrr")except UserInputException as ue:    print( "exception:", ue.name )
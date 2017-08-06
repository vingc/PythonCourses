#! python

def printMax(a, b):
    '''Print the maximum of two values

    the two values must be integer.'''
    
    if a < b:
        print(a)
    else:
        print(b)

    return

printMax(2, 3)
print(printMax.__doc__)
help(printMax)

#! python

age = 25
name = 'Swaroop'

print('{0} is {1} years old\n'.format(age, name)) #Swaroop is 25 years old
print('{0:.3}'.format(1/3)) #0.333
print('{0:_^11}'.format("hello")) #___hello___
print('{a1} is test'.format(a1=name))

x = 12*2
y = 10/5

s = 'The value of ' + str(x) + '+' + repr(y) + ' is ' + str(x+y)
print(str(s))
print(repr(s))

k = repr("hello")
print(k+','+str(k))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:3d}'.format(x,x*x,x*x*x))



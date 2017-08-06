#! python

class Robot:
    '''Robot class, with a name.'''
    __factory = "Home" #private var
    _date = "2012"

    population = 0
    def __init__(self, name):
        '''Init the self variables.'''

        self.name = name
        print( "Robot {0} is created".format(self.name) )
        #increase the class variable
        Robot.population += 1
        
    def sayHi( self ):
        print( "Robot {0} give you a hug".format(self.name) )

    def __del__( self ):
        '''Swap the tail when delete a robot.'''
        print( "Robot {0} is destroied".format(self.name) )

        Robot.population -= 1

        if Robot.population == 0:
            print( "Robot {0} is the last one destroied".format(self.name) )
        else:
            print( "There are still {0} Robots".format(Robot.population) )

    @staticmethod
    def howMany():
        print("Cur have {} robots".format(Robot.population))

    #howMany = staticmethod(howMany)

rob1 = Robot("C1")
Robot.howMany()

rob2 = Robot("C2")
Robot.howMany()

del rob2
del rob1

Robot.howMany()
print("pri:", Robot._date )
#print("Private:", Robot.__factory)

class humanKiller(Robot):
    def __init__(self, name, weight):
        Robot.__init__(self, name)
        self.weight = weight
        print("Constructor humanKiller.", name)

    def __del__(self):
        Robot.__del__(self)

    def fire(self):
        Robot.sayHi(self)
        print("Robot {0} give u a bullet".format(self.name))

hk = humanKiller("Slaughter", 23)
hk.fire()

del hk
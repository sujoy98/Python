class Car:
    
    #  Class(Static) Variable
    wheels = 4
    
    def __init__(self):
        
        #  Instance Variable
        self.mil = 10

c1 = Car()
c2 = Car()

c1.mil = 11
Car.wheels = 10

print(c1.mil, c2.mil)
print(c1.wheels, Car.wheels)
class Robot:
    def __init__(self, Name, Color, Weight):
        self.Name = Name
        self.Color = Color
        self.Weight = Weight

    def introduce_self(self):
        print("My name is " + self.Name)
        print("My color is " + self.Color)
        # can only concatenate str (not "int") to str so we type cast to string i.e str
        print("My weight is " + str(self.Weight))
r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

r1.introduce_self()
r2.introduce_self()



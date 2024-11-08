#Instance: a specofoc occurance of a class
#constructor: creates an instance of a class



class Cat:
    def __init__(self, Name, Color):
        self.name = Name
        self.color = Color
        self.age = 0
        self.weight = 2
        self.intelligence = 0
        self.energy = 5
        self.happiness = 5
        self.anger = 0
x = input("Name:")
y= input("colour:")
c1 = Cat(x, y)
#print(c1.name)
#print(c1.color)
print(type(c1))
        
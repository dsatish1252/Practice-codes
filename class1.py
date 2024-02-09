class Bike:
     def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        print("object has created")
    def abc(self):
          print(self.x*self.y)


obj = Bike(1, 2, 3)
obj2 = Bike(int(input("enter a")),5,6)
print(obj.x)
print(obj.y)
print(obj.z)
print(obj.abc())
print(obj2.abc())
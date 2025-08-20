class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def x(self):
        print(f"{self.name} is a good boy,{self.age} years old")
a=human("yash",22)
a.x()        
        

# Create a Class:
# Write a class Mobile with attributes brand and price
# Create two objects of the class and display their attributes using a method.

class moblie:
    def __init__(self ,brand ,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"{self.brand} costs {self.price}")
m1 = moblie("mi",5000)
m2 = moblie("iphone",65000)
m2.display()           
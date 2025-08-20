class student:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def greet(self):
        print(f" {self.name} is {self.age} years old , he is from {self.place}")
x=student("yash",22,"periyapatna")

x.greet()
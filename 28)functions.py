def marriage(x,y):   #parameters
    print(f"boy is {x} ")
    print(f"girl is {y} ")
    print(f"{x} married {y}")
marriage("yash","push")  # positional arguments
marriage(x="raj" , y="ram")  #keyword arguments


# GREET FUNCTIUION:  write a function greet() that takes no arguments and print a greeting message
def greet():
    print("welcome to python")
greet()    

# PARAMETERIZED GREET: Write a funtion greet_user() that takes a name as input and prints a custom greeting
def greet_user(name):
    print(f"hello {name} welcome to python")
greet_user("yash")    
    

# SUM FUNCTION: Write a function add_numbers(a,b) that returns the sum of two numbers. Call this function with different values.
    

def add_numbers(a,b):
    return a + b
print(add_numbers(3,3))    
print(add_numbers(5.2,3))
print(add_numbers(200,7.8))  


# lambda function
add = lambda x ,y : x+y
print(add(1,5))

x = lambda x,y:x*y
print(x(2,6))



def yash(x,y):
    return x+y,x-y,x*y,x/y,x%y,x&y,x|y,x//y,x^y
print(yash(3,3))

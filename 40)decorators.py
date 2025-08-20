def yash(x):
    def wrapper(a,b):
        print("Result: ",end=" ")
        x(a, b)
    return wrapper

@yash
def add(a,b):
    print(a+b)
add(4,4)


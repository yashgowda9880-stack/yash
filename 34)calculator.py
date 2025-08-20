def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def div(a,b):
    return a / b
def mul(a,b):
    return a * b
while True:
    try:
        print("simple calculator")
        print("1 add")
        print("2 subtract")
        print("3 div")
        print("4 mul")
        print("5 quit")
        choice = int(input("enter your choice: "))

        if choice in {1,2,3,4}:
            a = int(input("enter the first number: "))
            b = int(input("enter the second number: "))

        if choice==1:
            print("Result: ",add(a,b))
            
        elif choice==2:
            print("Result: ",sub(a,b))
                
        elif choice==3:
            print("Result: ",div(a,b))

                
        elif choice==4:
            print("Result: ",mul(a,b))

        elif choice ==5: 
            print("exit") 
            print("\U0001F600"*10)
            break  
        
    except:
       
        print("invalid! choose correct option")
        print("__"*15)




# i created this calculater
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
while True:
    try:
        print("<<<<<<<  calculator  >>>>>>>>")
        print("01 addition: \n02 subtraction: \n03 quite")
        choice = int(input("enter your choice: "))
        if choice in {1,2}:
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
        if choice==1:
            print(a+b)
            print("___"*10)
        elif choice==2:
            print(a-b)
            print("___"*10)
    
        elif choice==3:
            print("exit")
            print("\U0001F600"*10)
            break
    except:
        print("invalid! choose correct option")


# using match case
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def div(a,b):
    return a / b
def mul(a,b):
    return a * b
while True:
        try:
            print("simple calculator")
            print("1 add")
            print("2 subtract")
            print("3 div")
            print("4 mul")
            print("5 quit")
            choice = int(input("enter your choice: "))
            match choice:
            

                case 1:
                    a = int(input("enter the first number: "))
                    b = int(input("enter the second number: "))
                    print("Result: ",add(a,b))
                    
                case 2:
                    a = int(input("enter the first number: "))
                    b = int(input("enter the second number: "))
                    print("Result: ",sub(a,b))    

                case 3:
                    a = int(input("enter the first number: "))
                    b = int(input("enter the second number: "))
                    print("Result: ",div(a,b))

                        
                case 4:
                    a = int(input("enter the first number: "))
                    b = int(input("enter the second number: "))
                    print("Result: ",mul(a,b))

                case 5: 
                    print("exit") 
                    print("\U0001F600"*10)
                    break  
            
        except:
            print("invalid! choose correct option")
        

x = int(input("enter a number: "))
if x %2==0:
    print("even")
else:
    print("odd")

# _______________________________________________________________________________________________________________________________________________________________________________________
while True:
    try:
        number = int(input("Num : "))
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    except:
        print("enter valid input")    

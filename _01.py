pin=123
attempt=0
while True:
    try:
        print("welcome to instagram")
        user_input = int(input("enter your insta pin: "))
        attempt+=1
        if user_input==pin:
            print("correct pin")
            break
        elif attempt==5:
            print("too many wrong attempts , try again later")
            break
        else:
            print(f"wrong pin try again {attempt}")
    except ValueError:
        attempt+=1
        print(f"enter valid input, pls try again {attempt} ")
        if attempt==5:
            print("your attempts are over")
            break
        

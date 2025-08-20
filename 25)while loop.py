 # print 1 to 10

x = 1 
while x<=10:   
    print(x)
    x+=1

 # write a program to print even number between 1 tp 20
 
x = 1             
while x<=20:
        print(x)
        x+=2    

# booking ticket 
total_seats = 3
while total_seats>0:
    total_seats-=1
    user_input = input("Type 'yes' to book a seat: ")
    if user_input == 'yes':
        print(f"booking confirmed.seat left is: {total_seats}")
    else:
        print("invalid input please type 'yes' to book a seat")
print("all seats are booked.")



total_seats = 2
while total_seats>0:
    user_input = input("press 'y' to book a seat: ")
    if user_input=='y':
        total_seats-=1
        print(f"your ticket is booked. Ticket left is : {total_seats}")
    else:
        print("invalid input press 'y' to book a seat")
print("No ticket is left")  


# count down 10 t0 1
import time
print("COUNT DOWN")
count = 10
while count>0:
    print(count)
    time.sleep(1)
    count-=1
print("happy new year")    


# atm pin

atm_pin = 1234
x = 3
while x>0:
    x-=1
    user_input = int(input("enter pin: "))

    if user_input==1234:
        print("coreect")
        break
    else:
        print("incorrect")
print("your attempts are over.")        

# INSTAGRAM PASSWORD

print("INSTAGRAM PASSWORD")
password = "yash"
attempts = 1
while attempts<=3:
    attempts+=1
    user_input = input("enter a password: ")
    if user_input=="yash":
        print("successfull you can login")
        break
    else:
        print("try again")
print("your attempts are over")        
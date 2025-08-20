user_age = int(input("User Age: "))
if user_age >=18:
    print("your an adult")
else:
    print("you are minor")


print("SIGNAL")
user_choice = input("signal : ")
if user_choice == "red":     # WE CAN USE ELIF MULTIPLE TIMES
    print("Stop")
elif user_choice=="yellow":
    print("stay")
elif user_choice=="green":
    print("go")
else:
    print("ERROR")



print("BUS PASS")
person = int(input("person age:  "))
if person<=5:
    print("Bus pass is free")
elif person>=60:
    print("senior citizen discount")
else:
    print("Pay the full fees")    


print("check the time of a day")
time = int(input("Time: "))
if time==8:
    print("Breakfast")
elif time==13:
    print("lunch")
elif time==20:
    print("dinner")
else:
    print("its not a meal time")



print("LIBRARY MEMBERSHIP" )
person = int(input("Person_age : "))
if person<=18:
    print("you will get a student membership")
elif person>=60:
    print("you will get a senior citizen membership")
else:
    print("you will get a regular membership")
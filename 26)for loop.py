# sum of first 10 numbers
x = 0
for y in  range (1,11):
    x+=y
print(x)


#print your name latter by latter
user_name = input("enter your name: ")
for y in enumerate(user_name):
    print(y)



user_name = input("enter your name: ")
for index,y in enumerate(user_name):
    print(y*(index+1),end="  ")




 # COUNT NUMBER OF VOWELS IN STRING   
x = input("enter a string : ")
count = 0
vowels = "aeiouAEIOU"
for y in x:
    if y in vowels:
        count+=1
        print(count)   

# read
x = open("yash.txt","r")
y =x.read()
print(y)
x.close()

# or , using with
with open ("yash.txt",'r')as yash:
    x=yash.read()
print(x)

# write
x = open("yash2.txt",'w')
x.write("yash\n")
x.write("push")
print(x)
x.close()

# append
x = open("yash2.txt",'a')
x.write("yash\n")
x.write("rash")
print(x)
x.close()


# create a new file safely
x

# with
with open("yash3.txt",'w') as file:
    file.write("yash\n")
    file.write("push")
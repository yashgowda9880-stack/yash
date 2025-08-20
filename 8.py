Message = "this is a warning!  "
print(Message.upper())
print(Message.lower())
print(Message.strip()*3)
print(Message.replace("warning", "Error"))

name = "yashgowda"

print(name[4:]) #index = position -1
print(name[:4])
print(name[2:4])
print(name[:])
print(name[::2])


# Escape sequence
a = "yash is \n a good boy"
print(a)

a = "yash is \t a good boy"
print(a)

a = "yash is \\ a good boy"
print(a)
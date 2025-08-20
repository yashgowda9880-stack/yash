# output is 2
a = [1,2,3,4,5,6,7,8,9]
b = a[1]
print(b)

# output is [2,3,4,5,6,7,8,9]
a = [1,2,3,4,5,6,7,8,9]
b = a[1:]
print(b)

# output is [2,4,6,7]
a = [1,2,3,4,5,6,7,8,9]
b = a[1::2]
print(b)

# output is reverse
a = [1,2,3,4,5,6,7,8,9]
b = a[::-1]
print(b)

# output is [2]
a = [1,2,3,4,5,6,7,8,9]
b = a[:1]
print(b)

# output is [1,3,5,7,9]
a = [1,2,3,4,5,6,7,8,9]
b = a[::2]
print(b)
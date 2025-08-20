gender = ("yash",)  # tuple
print(type(gender))

tuple = (10,20,30,40,50)  # tuple
y = tuple[1:3]
print(y)
tuple2 = (60,)
x = tuple + tuple2
print(x)

yash = ["xx",'yy',"zz"] # tuple adding two tuples because it doesnot allow 'add' keyword
x = tuple(yash)
yash2 = ["tt"]
y = yash +yash2
print(y)

s = {300,1,32} # sets are unordered
print(type(s))


s = {1,2,3}   # sets
s.add(4)
s.remove(3)
print(s)
s.pop()
print(s)

yash = ["xx",'yy',"zz"]  #converting 'list' into 'set' and 'tuple'
x = set(yash)
y = tuple(yash)
print(type(x))
print(type(y))


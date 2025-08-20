# remove the spaces from the given string
x = input("enter a string: ")
y = x.replace(" ","")
print(y)

# remove duplicate elements from the list because set is orderd
x = [1,1,2,2,3,3,4,5]
y = list(set(x))
print(y)

#check if a string is palindrome in one line
print('madam'=='madam' [::-1])

while True:
    user_input = input("enter your word: ")
    if user_input==user_input[::-1]:
        print("pallindrome")
    else:
        print("not pallindroome")

while True:
    x = input("enter a word: ")
    print(x==x[::-1])

    l1 = [1,2,3]
l2 = [4,5,6]
for i in l1:
  for j in l2:
    print(i,j)
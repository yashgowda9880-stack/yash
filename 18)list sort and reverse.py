list = [50,20,30,10,40]
list.sort()
print(list)
list.reverse()
list.sort(reverse=True)
print(list)


l = [1,2,3,4]
dl = [num*2 for num in l]
print(dl)


x = input("enter list of integer : ").split()
l = [int(y) for y in x]
print(l)



student_info = [
   { "name" :"yash", "age" : 22, "marks" : 98},
    {"name" :"push", "age" : 22, "marks" : 98},
    {"name" :"rash", "age" : 22, "marks" : 98}
]
for student in student_info:
    print("NAME:" , student["name"])
    print("AGE:" , student["age"])
    print("MARKS:" , student["marks"])
    print("_"*20)    

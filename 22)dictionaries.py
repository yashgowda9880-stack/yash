city = {
    "mysore" : "biriyani",
    "manglore" : "fish fry",
    "banglore" : "ntg",
    "mandya" : "non veg",
    "kodagu" : "pork"
}
city["kolar"]="mutton"
print(city)
print("updating banglore dish....")
city["banglore"] = "ice cream"
print(city)
city.pop("mandya")
print(city)
print(city.get("goa","NOT FOUND"))
print(city)
print(city.keys())
print(city.values())

# second question
friend_one = {
    "name" : "raj",
    "favorite_food" : "any_veg",
    "favorite_subject" : "java"
}

friend_two = {
        "name" : "kumar",
    "favorite_food" : "non_veg",
    "favorite_subject" : "hindi"
}
print(friend_one["favorite_food"])



student = ["yash","push"]
marks = [50,60]
for i in range(2):
        student_mark ={}
        student_mark[student[i]] =[marks[i]]
        print(student_mark)
print(type(student_mark))



names = ["yash","push"]
x = {name:len (name) for name in names}
print(x)
       



city = {
    "mysore" : 50,
    "manglore" : 55,
    "banglore" : 10,
    "mandya" : 57,
    "kodagu" : 23
}
total_price = 0
for y in city.values():
    total_price += y
print("total price is : " ,total_price)        
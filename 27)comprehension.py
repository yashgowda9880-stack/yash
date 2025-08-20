numbers = [i for i in range(1,11)]
squares = [i**2 for i in range (1,11)]
print(numbers,squares)

for i in range (1,11):
    print(i**2)


kannada_city = {
    "mysore" : 30000,
    "mandya" : 35000,
    "kodagu" : 25000
}
filter_city = {x:y for x, y in kannada_city.items() if y>=27000}
print(filter_city)
    
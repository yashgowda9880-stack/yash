while True :print(eval(input(">>>")))
#  eval works like a caculator in python
# eval() take a string and evalues it as a python expressions

while True:
    print(eval(input("------>")))


while True:
     try: print(float(eval(input("------>"))))
     except: print("invalid input, pls try again")    
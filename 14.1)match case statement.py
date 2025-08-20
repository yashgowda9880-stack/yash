while True:
    time = int(input("enter the time: "))
    match time:
            case 8:
                print("breakfast")
                break
            case 10:
                print("read")
                break
            case 13:
                print("lunch")
                break
            case 16:
                print("snaks")
                break
            case 19:
                print("dinner")
                break
            case _:
                print("not a correct time")                       


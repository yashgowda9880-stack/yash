try:
    boy = input("who do you want to marry: ")   
    if boy.lower() != "yash":
        raise Exception("you have to marry yash. select him")
except Exception as e:
    print(f"Error: {e}")
else:
    print("yes! yash is ready")
finally:
    print("end")    


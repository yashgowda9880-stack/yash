is_student = "Yes"
print(type(is_student))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    print("prime numbers from 0 to 10: ")
    for num in range(11):
        if is_prime(num):
            print(num)

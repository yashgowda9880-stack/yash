# factorial of a number
def factorial(n):
    if n == 1:
        return n
    else:
        return n  * factorial(n - 1)
print(factorial(5))

# calculate the sum of first n numbers

def first_n_numbers(n):
    if n == 1:
        return n
    else:
        return n   + first_n_numbers(n - 1)
print(first_n_numbers(5))
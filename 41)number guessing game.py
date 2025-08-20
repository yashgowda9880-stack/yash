import random
def number_guessing_game():
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("welcome to yash game's")
    print("im thinking of a number between 1 to 100")
    while True:
        try:
            guess = int(input("enter your guess: "))
            attempts+=1
            if guess< number_to_guess:
                print("too low! , try again")
            elif guess> number_to_guess:
                print("too high! , guess again")
            else:
                print(f"congratylations! your guessed in {attempts} attempts")
                break
        except ValueError:
            print("invalid! enter a valid number.")
number_guessing_game()               

import random
def rock_paper_scissors():
    options=("rock","paper","scissors")
    print("Type 'rock','paper','scissors' to start a game, Type 'quit' to end the game")
    while True:
        user_choice = input("your choice: ").lower()
        if user_choice==quit:
            print("Thank you for playing yash's game")
            break
        if user_choice not in options:
            print("Invalid! please choose rock,paper or scissors")
            continue
        computer_choice=random.choice(options)
        print(f"Computer chooses {computer_choice}")
        if computer_choice==user_choice:
            print("its a tie")
        elif (
                (user_choice=='rock' and computer_choice=='scissors')
                or
                (user_choice=='scissors' and computer_choice=='paper')
                or
                (user_choice=='paper' and computer_choice=='rock')):
            print("congratulation you won")
            break
        else:
            print("you lose!")
rock_paper_scissors()            

                    
                    
            

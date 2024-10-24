import random

exit = False
user_point = 0
computer_point = 0


while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print('Your input is rock')
            print("Computer inout is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins")
            computer_point +=1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is paper")
            print("You win ")
            user_point +=1

    elif user_input == "paper":
        if computer_input == "rock":
            print('Your input is scissors')
            print("Computer inout is rock")
            print("You win")
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("Its a tie")
            computer_point +=1
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is paper")
            print("Computer wins")
            user_point +=1

    elif user_input == "scissors":
        if computer_input == "rock":
            print('Your input is scissors')
            print("Computer inout is rock")
            print("Computer wins")
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("Its a You win")
            computer_point +=1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is paper")
            print("Its a tie")
            user_point +=1





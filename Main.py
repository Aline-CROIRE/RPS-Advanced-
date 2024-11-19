import random
user_wins= 0
computer_wins= 0
options=["rock","paper","scissor"]

while True:
    user_choice=input("Choose Rock,Scissor,Paper or q to quit  ").lower()

    if user_choice not in options:
        break
    if user_choice =="q":
        quit()
    random_number=random.randint(0,2)
    computer_choice=options[random_number]

    print(f"You Choose {user_choice} .")
    print(f"Computer Choose {computer_choice} .")

    if(user_choice==computer_choice):
        print("its a draw!!")

    elif user_choice == "rock" and computer_choice== "scissor":
        print("You win!")
        user_wins+=1
    elif user_choice== "paper" and computer_choice=="rock":
        print("You win!")
        user_wins += 1
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You win!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins+=1
print(f"You Won {user_wins} times.")
print(f"computer Won {computer_wins} times.")
print("Good Bye!!!")





import random

user_choice = input("what do you choose? Type 0 for rock ,1 for paper or 2 for scissor. \n ")
computer_choice = random.randint(0, 2)
print(f"Computer_ chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")
else:
    print(" you typed an invalid number, you lose!")
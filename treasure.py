print("Welcome to Treasure Island \n Your mission is to find the Treasure.")
turn1 = input("which turn would you like to take? left or right")
if turn1 == "left":
    turn2 = input("would you like to wait or swim? ")
    if turn2 == "wait":
        turn3 = input("which door you wanna choose red blue or yellow?")
        if turn3 == "yellow":
            print("you win")
        elif turn3 == "blue":
            print("game over")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("Game Over")
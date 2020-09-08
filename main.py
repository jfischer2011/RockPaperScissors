from random import randint


# Options
t = ["Rock", "Paper", "Scissors"]

# assign random play to computer
computer = t[randint(0, 2)]

# set player to false
player = False
# game play
while player == False:
    player = input(" Choose Rock, Paper, or Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print(computer, "covers", player, "You lose :( ")
        else:
            print(player, "crushes", computer, "YOU WIN!!")
    elif player == "Paper":
        if computer == "Scissors":
            print(computer, "cuts", player, "You lose :( ")
        else:
            print(player, "covers", computer, "YOU WIN!!")
    elif player == "Scissors":
        if computer == "Rock":
            print(computer, "crushes", player, "You lose :( ")
        else:
            print(player, "cuts", computer, "YOU WIN!! ")
    else:
        print("Please choose between Rock, Paper and Scissors. Check your spelling!")

    player = False
    computer = t[randint(0 , 2)]



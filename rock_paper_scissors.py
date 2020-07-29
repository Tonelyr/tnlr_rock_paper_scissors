import random as r

# Define playable options
rps = ["Rock", "Paper", "Scissors"]

# Generate random options from rpc
comp = rps[r.randint(0,2 )]

player = False

while player == False:
    player = input("Rock, Paper, Scissors ? ")
    if player == comp:
        print("Tie !")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose !", comp, "covers", player)
        else:
            print("You win !", player, "covers", comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose !", comp, "cut", player)
        else:
            print("You win !", player, "covers", comp)
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose !", comp, "smashes", player)
        else:
            print("You win !", player, "cut", comp)
    else:
        print("Incorrect Value")

input("Do you want to play again ? (Y/N) ")

if input == "Y" or "y":
    player = False
else:
    print("Bip boup, shutting down...")
while player == False:
    player = input("Rock, Paper, Scissors ? ")
    if player == comp:
        print("Tie !")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose !", comp, "covers", player)
        else:
            print("You win !", player, "covers", comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose !", comp, "cut", player)
        else:
            print("You win !", player, "covers", comp)
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose !", comp, "smashes", player)
        else:
            print("You win !", player, "cut", comp)
    else:
        print("Incorrect Value")
print("Bip boup, shutting down....")

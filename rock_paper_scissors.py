import random



print("===================")
print("Rock Paper Scissors")
print("===================")

print("1)" "✊")
print("2)" "✋")
print("3)" "✌")
print("4)" "🦎")
print("5)" "🖖")

while True:
    player = int(input("Pick a number: "))
    computer = random.randint(1,5)
    print(f"You chose: {player}")
    print(f"CPU chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == 1 and computer == 2:
        print("Computer won!")
    elif player == 1 and computer == 3:
        print("The player won!")
    elif player == 1 and computer == 4:
        print("The player won!")
    elif player == 1 and computer == 5:
        print("Computer won!")
    elif player == 2 and computer == 1:
        print("The player won!")
    elif player == 2 and computer == 3:
        print("Computer won!")
    elif player == 2 and computer == 4:
        print("Computer won")
    elif player == 2 and computer == 5:
        print("The player won!")
    elif player == 3 and computer == 1:
        print("Computer won!")
    elif player == 3 and computer == 2:
        print("The player won!")
    elif player == 3 and computer == 4:
        print("The player won!")
    elif player == 3 and computer == 5:
        print("Computer won")
    elif player == 4 and computer == 1:
        print("Computer won!")
    elif player == 4 and computer == 2:
        print("The player won!")
    elif player == 4 and computer == 3:
        print("Computer won!")
    elif player == 4 and computer == 5:
        print("The player won!")
    elif player == 5 and computer == 1:
        print("The player won!")
    elif player == 5 and computer == 2:
        print("Computer won!")
    elif player == 5 and computer == 3:
        print("The player won!")
    elif player == 5 and computer == 4:
        print("Computer won!")

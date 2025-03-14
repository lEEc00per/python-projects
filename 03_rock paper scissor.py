import random
is_running = True
while is_running:
    computer = random.choice([1, -1, 0])
    youstr = input("Enter your choice: ")
    youDict = {"r": 1, "s": -1, "p": 0}
    reverseDict = {1: "Rock", -1: "Scissor", 0: "Paper"}

    you = youDict[youstr]
    # By now we have twon numbers (variables), you and the computer

    print(f"You chose {reverseDict[you]}\nand computer chose {reverseDict[computer]}")
    if (computer == you):
        print("It is a draw")
    else:
        if((computer - you) == -1 or (computer - you) == 2):
            print("You Lose!")
        elif ((computer - you) == 1 or (computer - you) == -2):
            print("You won!")
        else:
            print("Something went wrong!")
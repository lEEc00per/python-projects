print("Welcome To The QUIZ GAME")
def quiz():
        answer = input("What does CPU stand for? ")
        if answer == "central processing unit":
            print("Correct!")
        elif answer != "central processing unit":
            print("Incorrect!")

        answer = input("What is the longest word in the English language? ")
        if answer == "pneumonoultramicroscopicsilicovolcanoconiosis":
            print("Correct!")
        elif answer != "pneumonoultramicroscopicsilicovolcanoconiosis":
            print("Incorrect!")

        answer = input("If John is taller than Mike, and Mike is taller than Tom, who is the shortest? ")
        if answer == "tom":
            print("Correct!")
        elif answer != "tom":
            print("Incorrect!")
        
        answer = input("What non-living thing is a living thing? ")
        if answer == "shoes":
            print("Correct!")
        elif answer != "shoes":
            print("Incorrect!")

        answer = input("What has keys but can't open locks? ")
        if answer == "piano":
            print("Correct!")
        elif answer != "piano":
            print("Incorrect!")

        answer = input("Rearrange the letters in \"NEW DOOR\" to make one word. What is it(write in capital letters)? ")
        if answer == "ONE WORD":
            print("Correct!")
        elif answer != "ONE WORD":
            print("Incorrect!")

        answer = input("What word is spelled incorrectly in every dictionary? ")
        if answer == "incorrectly":
            print("Correct!")
        elif answer != "incorrectly":
            print("Incorrect!")


is_running = True
while is_running:
    playing  = input("Do you want to play the game? ")
    if playing == "yes":
        print("Okay Let's play the game :)")
        quiz()

    elif playing == "no":
        print("Bye!")
        quit()
    else:
        print("Please enter yes or no")

'''
Nim Newest Version
Maxim Rebguns
V2.0.1
'''

##Imports
import time

##Variable playing is true until the user quits the game
playing = True

#run() the function that contains the main part of the game 
def run():
    lost = False                                                                                ##lost is the variable that is false until the computer loses
    approved = False                                                                            ##Approved variable only becomes true once the input is a valid number
    while not approved:                                                                         ##While loop checks if the input is valid (a natural number)
        try:
            white_beans = int(input("How many white beans do you want in the game?  "))         ##Variable stores amount of white beans in the game
            if white_beans <= 0:
                print("")
                print("How about a positive number (no decimals)")
                print("")
            else:
                print("")
                approved = True
        except:
            print("")
            print("Please choose a positive integer. (1, 2, 3, ...)")
            print("")
    print("")                                                                                   ##Spacing between the text lines
    approved = False                                                                            ##Explained above
    while not approved:                                                                         ##Explained above
        try:
            turn = int(input("Choose the maximum number of beans to take per turn:  "))
            if turn <= 0:
                print("")
                print("How about a positive number (no decimals)")
                print("")
            elif turn > white_beans:
                print("")
                print("You can't take more beans than there are!")
                print("")
            else:
                print("")
                approved = True
        except:
            print("")
            print("Please choose a positive integer. (1, 2, 3, ...)")
            print("")
    print("Okay. You chose to take 1 - %s beans per turn" % turn)                               ##Line of text confirming number of beans
    print("")
    even = turn + 1                                                                         
    remainder = white_beans % even
    if remainder != 0:
        print("I will go first.")
        print("HAHAHA, let me think...")
        time.sleep(3)
        print("I will take %s beans" % remainder)
        white_beans -= remainder
        print("")
        print("There are now %s white beans" % white_beans)
        print("")

        
    while white_beans != 0:
        print("Now your turn!")
        approved = False
        while not approved:
            try:
                player = int(input("How many white beans do you take?  "))
                if player <= 0:
                    print("")
                    print("How about a positive number (no decimals)")
                    print("")
                elif player > turn:
                    print("Cheater! You said there would be 1 - %s beans per turn!" % turn)
                else:
                    print("")
                    approved = True
            except:
                print("")
                print("Please choose a positive integer. (1, 2, 3, ...)")
                print("")
        white_beans -= player
        print("")
        print("There are now %s white beans" % white_beans)
        print("")
        if white_beans == 0:
            print("What? How did I lose? That's imposible!")
            lost = True
            break
        print("Now my turn")
        print("Let me think...")
        time.sleep(3)
        robot = even - player
        white_beans -= robot
        print("I take %s beans" % robot)
        print("")
        print("There are now %s white beans" % white_beans)
        print("")

    if not lost:
        print("I won. I knew it. I knew it. HAHAHAHAHAHAHAHA")



#Main game loop
print("NIM V2.0.1")
print("Maxim Rebguns")
print("_"*20)
print("")
while playing:
    approved = False
    while not approved:
        try:
            instructions = input("If you know how to play, push enter. If you need the instructions, type 'i':  ")
            if instructions == 'i':
                print("Nim is a very simple game you can play at any time. There is a certain amount of white "
                      "beans and 1 black bean. Every turn you take a certain amount of beans, for example 1-5 beans. "
                      "Play continues until there are no more white beans left, so the player must take a black bean. "
                      "The person who has to take the black bean loses.")
                input("Push enter to start playing  ")
                approved = True
            else:
                approved = True
        except:
            print("Please type something")
    print("")
    run()
    print("")
    try:
        again= input("Please play again! I really want to beat you! Type 'a' to play again. Push enter to end the game:  ")
        if again == 'a':
            print("Yay!")
            print("")
            print("")
        else:
            print("Thanks for playing!")
            playing = False
    except KeyboardInterrupt:
        print("Thanks for playing!")
        playing = False

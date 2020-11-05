'''
Nim V1.0.1 2019
Maxim Rebguns
'''

def run():
    approved = False
    while approved == False:
        bean_num = int(input("Choose the number of beans to play with:  "))
        if bean_num < 0:
                print("Come on, seriously! The number of beans can't be negative. Try again.")
        else:
            approved = True
    approved = False
    while approved == False:
        maxa = int(input("Choose the maximum number of beans to draw each turn:  "))
        if maxa < 0:
                print("Come on, seriously! The number of beans can't be negative. Try again.")
        else:
            approved = True
    first_move = bean_num % maxa
    if first_move == 0:
        print("")
        print("You have the first move!")
        approved = False
        while approved == False:
            player1_move = int(input("Choose to take 1 - %s beans:  "% maxa))
            if player1_move > maxa:
                print("I said 1 - %s beans! Try again."%maxa)
            else:
                approved = True
        bean_num -= player1_move
        print("")
        print("There are now %s white beans" % bean_num)
        print("")
        print("Now my turn!")
        move2 = maxa - player1_move
        print("I will take %s beans" % move2)
        bean_num -= move2
    else:
        print("")
        print("I move first")
        print("I will take %s beans" % first_move)
        bean_num -= first_move
        
    

    while bean_num != 0:
        print("")
        print("There are now %s white beans" % bean_num)
        print("")
        print("Now your Turn!!!!")
        approved = False
        while approved == False:
            player1 = int(input("How many beans do you take '1-%s':  " % maxa))
            if player1 > maxa:
                print("I said 1 - %s beans! Try again."%maxa)
            else:
                approved = True
        bean_num -= player1
        if bean_num == 0:
            print("You win! Ah, man, I got the black bean")
        print("")
        print("There are now %s white beans" % bean_num)
        print("")
        print("I move!")
        robot = maxa - player1
        print("I take %s beans" % robot)
        bean_num -= robot
    print("There are now %s white beans" % bean_num)
    print("I won. You have to take the black bean. HAHAHAHAHAHHAHAHAHAHAHHAHAHA")
    

playing = True
print("Nim")
print("Version 1.0.1")
print("Maxim Rebguns")
print("-------------------------------")
print("Welcome to nim, the game of logic")
instructions = input("Type 'I' if you want to read the instructions. Push enter to skip:  ")
if instructions == "I":
    print("")
    print("You choose the amount of white beans to play with. There is one black bean.")
    print("Each player draws a certain amount of beans each turn. If you get the black bean, you lose.")
    print("")
    play = input("Type enter to play  ")
while playing:
    run()
    print("Please play again. I really really want to beat you")
    again = input("Push enter to leave the game. To play again, type a:  ")
    if again == "a":
        playing = True
    else:
        playing = False

'''
Nim V1.0.1 2019
Maxim Rebguns
run()
'''
def run():
    bean_num = int(input("Choose the number of beans to play with:  "))
    first_move = bean_num % 4
    if first_move == 0:
        print("")
        print("You have the first move!")
        player1_move = int(input("Choose to take 1 - 3 beans:  "))
        bean_num -= player1_move
        print("")
        print("There are now %s white beans" % bean_num)
        print("")
        print("Now my turn!")
        move2 = 4 - player1_move
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
        player1 = int(input("How many beans do you take '1-3':  "))
        bean_num -= player1
        if bean_num == 0:
            print("You win! Ah, man")
            break
        print("")
        print("There are now %s white beans" % bean_num)
        print("")
        print("I move!")
        robot = 4 - player1
        print("I take %s beans" % robot)
        bean_num -= robot

    

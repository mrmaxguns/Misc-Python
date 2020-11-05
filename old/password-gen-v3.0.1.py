'''
Password Generator
V3.0.l
Maxim Rebguns
'''

import random
from proofread import *

err = "Please select a natural number!"

def run():
    def generate(c, cap, numb, x):
        first = random.randint(1,2)
        if first == 1:
            vowel = True
        if first == 2:
            vowel = False
        passw = [1]
        if cap:
            passw.append(2)
        if numb:
            passw.append(3)
        if x:
            passw.append(4)
        caps_v = "AEIOU"
        caps_c = "QWRTYPSDFGHJKLZXCVBNM"
        lower_v = "aeiou"
        lower_c = "qwrtypsdfghjklzxcvbnm"
        num = "1234567890"
        xtra = "!@#$%^&*()_-+={}[]:;'<>?,./"
        password = []
        print("")
        for _ in range (c):
            char = random.choice((passw))
            if char == 1:
                if vowel == True:
                    password.append(random.choice(lower_v))
                    vowel = False
                if vowel == False:
                    password.append(random.choice(lower_c))
                    vowel = True
            if char == 2:
                if vowel == True:
                    password.append(random.choice(caps_v))
                    vowel = False
                if vowel == False:
                    password.append(random.choice(caps_c))
                    vowel = True
            if char == 3:
                password.append(random.choice(num))
            if char == 4:
                password.append(random.choice(xtra))
        return ''.join(password)

    #amount = int(input("How many characters do you want in your password?  "))
    amount = integer_check("How many characters do you want in your password?  ", "x", "err", 1, err, err)
    if amount > 10000:
        areyousure = input("WARNING! Are you sure you want to proceed? This long of a password may slow your computer. Continue? Type n to quit. ")
        if areyousure == "n":
            quit()
    capitals1 = input("Do you want to include capitals? y/n  ")
    if "y" in capitals1:
        capitals = True
    else:
        capitals = False
    numbers1 = input("Do you want to include numbers? y/n  ")
    if "y" in numbers1:
        numbers = True
    else:
        numbers = False
    xtrachars1 = input("Do you want to include other characters? y/n  ")
    if "y" in xtrachars1:
        xtrachars = True
    else:
        xtrachars = False
    print(generate(amount, capitals, numbers, xtrachars))

print("Welcome to password generator Version 3")
run()


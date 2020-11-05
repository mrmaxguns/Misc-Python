'''
Password Generator
V3.0.l
Maxim Rebguns
'''

import random
from proofread import *
import itertools

err = "Please select a natural number!"
err2 = "Please answer yes or no"

def sec(password):
    xtra_character_approval = False
    caps_approval = False
    number_approval = False
    xtra = "!@#$%^&*()_-+={}[]:;'<>?,./"
    faults = []
    xtrac = []
    #integers
    '''
    for inte in password:
        integers = str.isdigit(inte)
        if integers == True:
            number_approval = True
            break
    '''
    character_in_pass = 1
    number_approval = False
    checking = False
    while not checking:
        try:
            integers = str.isdigit(password[character_in_pass])
            if integers:
                number_approval = True
                checking = True
            character_in_pass += 1
        except IndexError:
            checking = True
    if number_approval == False:
        faults.append("at least one number")
            
    #Xtra characters
    for c in xtra:
        xtrac.append(c)
    for x in xtrac:
        if x in password:
            xtra_character_approval = True
            break
    if xtra_character_approval == False:
        faults.append("extra characters")
    #Length
    if len(password) < 8:
        faults.append("the length of your password is less than 8 characters long")
    #Uppercase
    for uppercase in password:
        if uppercase.isupper() == True:
            caps_approval = True
            break
    if caps_approval == False:
        faults.append("at least one capital letter")
    percentage = 4 - len(faults)
    percentage *= 25
    faults_to_fix = ', '.join(faults)
    faults_to_fix = ("Your password is missing "+faults_to_fix)
    if faults_to_fix == "Your password is missing ":
        return "Your password is 100% secure"
    else:
        faults_to_fix = faults_to_fix + ". Your password is only %s percent secure"%percentage
        return faults_to_fix

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


        alphafreq_c = ["b" , ["d",]*4 , ["f",]*2 , ["g",]*2 , ["h",]*6 , "j"   , "k"   ,
            ["l",]*4  , ["m",]*2 , ["n",]*7,["p",]*2 , "q"   , ["r",]*6 ,
            ["s",]*6  , ["t",]*9, "v"   , ["w",]*2 , "x"   , ["y",]*2 , "z"]

        alphafreq_v = [["a",]*8, ["e",]*13, ["i",]*7, ["o",]*8, ["u"]*3]

        alphafreq_c = list(itertools.chain.from_iterable(alphafreq_c))
        alphafreq_v = list(itertools.chain.from_iterable(alphafreq_v))
        upperfreq_c = [x.upper() for x in alphafreq_c]
        upperfreq_c = list(itertools.chain.from_iterable(upperfreq_c))
        upperfreq_v = [x.upper() for x in alphafreq_v]
        upperfreq_v = list(itertools.chain.from_iterable(upperfreq_v))

        caps_v = "AEIOU"
        caps_c = "QWRTYPSDFGHJKLZXCVBNM"
        lower_v = "aeiou"
        num = "1234567890"
        xtra = "!@#$%^&*()_-+={}[]:;'<>?,./"
        password = []
        print("")
        for _ in range (c):
            char = random.choice((passw))
            if char == 1:
                if vowel == True:
                    password.append(random.choice(alphafreq_v))
                    vowel = False
                elif vowel == False:
                    password.append(random.choice(alphafreq_c))
                    vowel = True
            if char == 2:
                if vowel == True:
                    password.append(random.choice(upperfreq_v))
                    vowel = False
                elif vowel == False:
                    password.append(random.choice(upperfreq_c))
                    vowel = True
            if char == 3:
                password.append(random.choice(num))
            if char == 4:
                password.append(random.choice(xtra))
        unsorted =  ''.join(password)
        list(unsorted)
        sorted1 = []
        for chara in unsorted:
            if str.isdigit(chara) == True:
                sorted1 = [chara] + sorted1
            elif chara in xtra:
                sorted1 = [chara] + sorted1
            else:
                sorted1.append(chara)
        sorted1 = ''.join(sorted1)
        return sorted1

    #amount = int(input("How many characters do you want in your password?  "))
    amount = integer_check("How many characters do you want in your password?  ", "x", "err", 1, err, err)
    if amount > 10000:
        areyousure = input("WARNING! Are you sure you want to proceed? This long of a password may slow your computer. Continue? Type n to quit. ")
        if areyousure == "n":
            quit()
    #capitals1 = input("Do you want to include capitals? y/n  ")
    capitals1 = yes_or_no_check("Do you want to include capitals? y/n  ", err2)
    #numbers1 = input("Do you want to include numbers? y/n  ")
    numbers1 = yes_or_no_check("Do you want to include numbers? y/n  ", err2)
    #xtrachars1 = input("Do you want to include other characters? y/n  ")
    xtrachars1 = yes_or_no_check("Do you want to include other characters? y/n ", err2)
    generated = generate(amount, capitals1, numbers1, xtrachars1)
    return(generated)

print("Welcome to password generator Version 3")
#run()
using = True
while using:
    generated = run()
    print(generated)
    print(sec(generated))
    try_again = input("Do you want to generate another? Type 'a' if you do. Otherwise just push enter ")
    if try_again != "a":
        using = False
print("Thanks for using this generator")


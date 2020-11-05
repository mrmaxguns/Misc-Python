'''
Password Generator
V1.0.l
Maxim Rebguns
'''
import random
def generate(c):
    chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    password = []
    print("")
    for _ in range (c):
        password.append(random.choice(chars))
    return ''.join(password)

print("Welcome to password generator Version 1")
amount = int(input("How many characters do you want in your password?  "))
print(generate(amount))


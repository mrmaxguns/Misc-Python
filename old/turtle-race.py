import turtle
import time
import random

#Control turtle monitors user's keypress
control = turtle.Screen()
control.title("TURTLE RACE!!!")

#The colors
aqua = "Aquamarine"
red = "red"
orangeish = "Coral"
pinkish = "Deep pink"
white = "white"

#Names all the turtles
bob = turtle.Pen()      #computer
lily = turtle.Pen()     #computer
john = turtle.Pen()     #computer
player = turtle.Pen()   #The player's turtle
chief = turtle.Pen()    #This turtle draws the race course

#Make chief invisible and set his speed to full
chief.hideturtle()
chief.speed(0)
chief.penup()

#Make the turtles trutle-shaped (except player)
bob.shape("turtle")
lily.shape("turtle")
john.shape("turtle")
player.shape("circle")

#Add color
bob.color(aqua)
lily.color(orangeish)
john.color(pinkish)
player.color(red)

#Bring the player's pens up
bob.penup()
lily.penup()
john.penup()
player.penup()

#SETUP
chief.goto(-250, 200)
chief.color(red)
chief.write("Turtle Race!", font = ("Arial", 20, "bold"))

chief.goto(100, 150)
chief.pendown()
chief.goto(100, -100)
chief.penup()
chief.goto(105, -100)
chief.pendown()
chief.write("Finish!", font = ("Arial", 10, "bold"))


bob.goto(-250 , 100)
lily.goto(-250, 50)
john.goto(-250, 0)
player.goto(-250, -50)

#COUNTDOWN
chief.penup()
chief.goto(-250, 130)
chief.pendown()
chief.write("3...", font = ("Arial", 50, "bold"))
time.sleep(1)
chief.color(white)
chief.write("3...", font = ("Arial", 50, "bold"))
chief.color(red)
chief.write("2...", font = ("Arial", 50, "bold"))
time.sleep(1)
chief.color(white)
chief.write("2...", font = ("Arial", 50, "bold"))
chief.color(red)
chief.write("1...", font = ("Arial", 50, "bold"))
time.sleep(1)
chief.color(white)
chief.write("1...", font = ("Arial", 50, "bold"))
chief.color(red)
chief.write("GO!!!", font = ("Arial", 50, "bold"))

def forward(speed):
    player.forward(speed)

#GAMEPLAY
while True:
    bob.forward(random.randint(1, 100)/50)
    lily.forward(random.randint(1, 100)/50)
    bob.forward(random.randint(1, 100)/50)

    #time.sleep(.001)

#Control monitors user's actions
control.listen()

'''
wn = turtle.Screen()
bob = turtle.Pen()
#bob.goto(0,0)

def yay():
    bob.forward(100)

wn.onkey(yay, "s")

wn.listen()
'''

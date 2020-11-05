import turtle

wn = turtle.Screen()
bob = turtle.Pen()
#bob.goto(0,0)

def yay():
    bob.forward(100)

wn.onkey(yay, "s")

wn.listen()

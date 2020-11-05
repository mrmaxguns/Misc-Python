import turtle

pen = turtle.Pen()
pen.speed(0)
pen.color("red")

for length in range(200):
    pen.forward(length)
    pen.right(100)


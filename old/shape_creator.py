import turtle
import proofread as pf

err = "Please choose a valid number"

print("Shape generator")
length = pf.integer_check("Choose the side length: ", "x", "none", 1, err, err)
amount_of_sides = pf.integer_check("Choose the amount of sides: ", "x", "none", 3, err+" greater than 2", err)

pen = turtle.Pen()

for _ in range(amount_of_sides):
    pen.forward(length)
    pen.right(360 / amount_of_sides)

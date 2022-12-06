# Nikolas S Fisher
#
# 11/1/2022
#
#
# This program will ask the user for the length of a side, a fill color, and what shape
# they would like to draw (square/triangle).
#
#

import turtle
Jerry = turtle.Turtle()
wn = turtle.Screen()
shapes = ["Triangle", "Square"]
print(shapes)
input1 = input("Pick a shape to draw:")
colors = ["Blue", "Green", "Purple", "Red"]

for i in colors:
    print(i)

input2 = str(input(print("Please pick a color:")))


#Jerry = turtle.Turtle()

if input1 == "Triangle":

    side1 = int(input("Length of bottom in pixels:"))
    Jerry.fillcolor(input2)
    Jerry.begin_fill()

    for i in range(3):
        Jerry.forward(side1)
        Jerry.left(120)
    Jerry.end_fill()

    #side1 = int(input(print("Length of 2nd side:")))
    #Jerry.forward(side1)


elif input1 == "Square":
    Jerry.fillcolor(input2)
    Jerry.begin_fill()
    sides = int(input("Pick the length of sides for Square"))
    for i in range(4):
        Jerry.forward(sides)
        Jerry.right(90)

    Jerry.end_fill()


wn.exitonclick()



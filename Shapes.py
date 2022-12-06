# Nikolas S Fisher
#
# Date: 11/15/2022
#
#
#
#
#
#
#

import turtle




def drawSquare(t, sz, z, x):
    """Get Turtle t to draw a square of sz side"""""
    alex.penup()
    alex.setposition(z, x)
    alex.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)

    #alex.penup()
    #alex.setposition(z, x)
    #alex.pendown()


wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

size=200
coordx=0
coordy=0

for i in range(6):
    drawSquare(alex, size, coordx, coordy)
    size-=40
    coordx+=20
    coordy+=20


# #alex.setposition(20,20)

# drawSquare(alex, 160, 20, 20)
# # #alex.setposition(40,40)
#
# drawSquare(alex, 120, 40, 40)
# # #alex.setposition(60,60)
#
# drawSquare(alex, 80, 60, 60)
# # #alex.setposition(80,80)
#
# drawSquare(alex, 40, 80, 80)


wn.exitonclick()
#
# Madison Blake
# 10-2-2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# 
import turtle
def main():
    turtle.hideturtle()
    square(100,0,50,'blue')
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
main()
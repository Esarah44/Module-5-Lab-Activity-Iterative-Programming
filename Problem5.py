# Turtle program that prints olympic symbol
# Sara Hernandez
# October 28, 2022
# This program will print the olympic symbol

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

alex.pensize(5)

alex.color("blue")
alex.penup()
alex.goto(-110, -25)
alex.pendown()
alex.circle(45)

alex.color("black")
alex.penup()
alex.goto(-10, -25)
alex.pendown()
alex.circle(45)

alex.color("red")
alex.penup()
alex.goto(90, -25)
alex.pendown()
alex.circle(45)

alex.color("yellow")
alex.penup()
alex.goto(-65, -75)
alex.pendown()
alex.circle(45)

alex.color("green")
alex.penup()
alex.goto(45, -75)
alex.pendown()
alex.circle(45)

wn.exitonclick()


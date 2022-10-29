# Turtle program to print polygons
# Sara Hernandez
# October 28, 2022
# This program will ask user for input on what polygon they would like to print

import turtle

polygon_sides = [int(input("Please enter the number of sides:"))]
length_side = int(input("Enter the length of the side:"))
color_side = input("Enter the color of the line:")
fill_polygon = input("Enter the fill color:")

wn = turtle.Screen()
alex = turtle.Turtle()

alex.begin_fill()

for i in range(polygon_sides[0]):
    alex.color(color_side)
    alex.forward(int(length_side))
    alex.left(int(360) / int(polygon_sides[0]))
    alex.fillcolor(fill_polygon)

alex.end_fill()

wn.exitonclick()
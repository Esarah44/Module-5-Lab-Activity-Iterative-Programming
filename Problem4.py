# Turtle program to print polygons
# Sara Hernandez
# October 28, 2022
# This program will ask user for input on what polygon they would like to print

import turtle

#polygon_sides = [int(input("Please enter the number of sides:"))]: no need to generate a list
polygon_sides = int(input("Please enter the number of sides:"))

length_side = int(input("Enter the length of the side:"))
color_side = input("Enter the color of the line:")
fill_polygon = input("Enter the fill color:")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(color_side, fill_polygon)
 
alex.begin_fill()

#for i in range(polygon_sides[0]): : repeat the loop for number of sides
for i in range(polygon_sides):
   # alex.color(color_side): use it once when to use begin_fill, end_fill
    alex.forward(int(length_side))
    #lex.left(int(360) / int(polygon_sides[0])): decide turning angle using sides
    alex.left(360/polygon_sides) 
   
   # alex.fillcolor(fill_polygon):use it once when to use begin_fill, end_fill

alex.end_fill()

wn.exitonclick()

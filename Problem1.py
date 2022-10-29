# if loop
# Sara Hernandez
# October 27, 2022
# The program ask the user to enter a number and prints "Hello World" by that number

answer = int(input("Enter a number (positive integer):"))
if answer >= 0:
    print(answer," Hello World!")
elif answer < 0:
    print("Error: Enter positive integer only")



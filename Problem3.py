# integers and divisible
# Sara Hernandez
# October 27, 2022
# for loop that prints integer, divisible by three, and divisible by seven

#for i in range(1, 50): #upper bound is exclusive
#    print(i)
#    if i % 3 == 0:
#        print("Divisible by three")
#    elif i % 7 == 0:
#        print("Divisible by seven")
        
for i in range(1, 51):    
    #You should check if the number is divisible by both first
    if i % 3 == 0 and i % 7 ==0:
        print("Divisible by both")
    elif i % 3 == 0:    #if not, then check if the number is divisible by three only
        print("Divisible by three") 
    elif i % 7 == 0:    #check the rest of numbers if divisible by seven
        print("Divisible by seven")
    else:
        print(i)        #none of the cases applies, then print a number as it is.
    


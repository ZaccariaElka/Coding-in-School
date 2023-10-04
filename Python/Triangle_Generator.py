
import time
import os

def triangle():
    Symbol = "[]"
    Space = "  "

    print("Inset one of these number: 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47") 

    number = input() #reads what the user writes in the console
    width = int(number) #converts the input into a number

    if width == 5 or width == 7 or width == 11 or width == 13 or width == 17 or width == 19 or width == 23 or width == 29 or width == 31 or width == 37 or width == 41 or width == 43 or width == 47:

        for y in range(width): #for loop (y)
            
            for x in range(width): #for loop (x)

                prime_number = (y * 2) + 1 #find the prime number for the triangle
                half_triangle = width / 2 #find the half of the triangle's width
                loop_width = width - 1 #the loop starts from 0 so we remove a value from the width

                if x > (loop_width - prime_number) / 2 and x < half_triangle and y < half_triangle or x <= ((loop_width) / 2 + prime_number / 2) and y < half_triangle and x >= half_triangle:
                
                    print(Symbol, end="") #if the statements are true it's gonna print the symbol
                else:
                    print(Space, end="") #prints a space into the console
                
            print() #goes ahead
    else:
        print("Invalid Number.") #prints message if the number is not valid
        time.sleep(2) #waits 2 seconds
        os.system('cls') #clears console
        triangle() #executes the function
        




triangle() #i used a function to make the whole code repeat if the user interts an invalid number. I could have used other ways but i wanted to try this one
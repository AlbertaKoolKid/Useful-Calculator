#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#import required modules

import math
import random

#define functions
def clearline(n):       
    """This is the clear line function
    
    This function takes an integer and prints that many blank lines in the 
    window.
    """
    for x in range(n):  
        print()

def surarea():
    """This is the function for calculating surface area. 
    
    This function will calculate the surface area of a handful of different 
    objects. It is self contained and doesn't referenct outside functions.
    """
    
    print("\n\n\nHere is a list of currently coded shapes.\n"
          "'rectangle' 'circle' 'triangle' \n\n")
    shape = input("What is the shape you are trying to calculate?   ")
    
    if shape == "rectangle": 
        l = int(input("What is the length?   "))
        h = int(input("What is the height?   "))
        sa = l*h
        print("\n\nThe surface area of the rectangle is " 
              + str(sa) 
              + " units squared.\n\n")        
    
    elif shape == "circle":                                                                         
        pi = math.pi
        r = int(input("What is the radius of the circle?   "))
        sa = pi*(r**2)
        print("\n\nThe surface area of the circle is " 
              + str(sa) 
              + " units squared.\n\n")           
    elif shape == "triangle":
        b = int(input("What is the base of the triangle?   "))
        h = int(input("What is the height of the triangle?   "))
        a = b*h/2
        print("\n\nThe surface area of the triangle is "
              + str(a) 
              + " units squared.\n\n")            
    else:
        print("\n\nThis shape is not added yet please let the author know.\n\n")
        return

def percent():
    print("\n\n\nThis works by taking a first number which is the "
          "position you are at,\n"
          "and a second number which is the total amount of places.\n\n"
          "For example if you entered the numbers 5 and 15 you would"
          "be shown that \n"
          "you are 33 percent through and the ratio is 5/15.\n\n\n")
    x = int(input("What is the number for the current positon?   "))
    y = int(input("What is the number for the total?   "))
    z = x*100/y
    print("\n\n\nYou are currently " +str(z)+ " percent through.\nThe ratio is " +str(x)+ "/" +str(y)+ ".\n\n\n")
    return

def volume():
    print("\n\n\nHere are a list of currently coded shapes.\n'cube'\n\n\n")
    shape = input("What is the shape you are trying to calculate?   ")
    if shape == "cube":
        l = int(input("What is your side length?   "))
        v = l**3
        print("\n\nThe volume of this cube is " + str(v) +	 " units.\n\n")
    else:
        print("\n\nNot a valid option\n\n")

def fahrenheit():
    cel = int(input("What is the current degrees Celsius?   "))#gets current temperature and sets in to be an integer
    fah = (cel*9/5)+32              #formula for calculating fahrenheit from celsius
    print("\n\nIt is currently "+str(fah)+" degrees Fahrenheit.\n\n")  #prints the string with the interrjection of the output variable as a string
    return

def celsius():
    fah = int(input("What is the current degrees Fahrenheit?   ")) #gets current teperature and sets in be an integer
    cel = (fah-32)*5/9 #formula to calculate celcius from fahrenheit
    print("\n\nIt is currently "+str(cel)+" degrees Celsius\n\n") #prints the string with the interjection of the output variable as a string
    return

def fractodec(): #not an easy formula. 
    print ("not yet implemented")
    return

def startup():
    """Here lies the main menu
    
    """
    clearline(10)
    print("Welcome to the Useful Calculator.\n"
          "With this program you will be able to calculate many different "
          "formulas to find your missing number.\n\n\n"
          "Type 'surface area' to calcualte the surface area of different objects.\n"
          "Type 'volume' to calculate the volume of different objects.\n"
          "Type 'percentage' to calculate the percentage of the numbers you have.\n"
          "Type 'fahrenheit' to calculate Fahrenheit from Celsius.\n"
          "Type 'celsius' to calculate Celsius from Fahrenheit.\n"
          "Type 'end' to quit the calculator and retrieve the save data.\n"
          )
    running = True
    while running == True:
        clearline(3)
        funInput1 = input("What would you like to do?   ") #asking for input
        funInput = funInput1.lower() #forcing the inputed string to become all lowercase
        if funInput == "percentage" or funInput == "per": #check if input is equal to the string if so run the function
            percent()             #run the function
        elif funInput == "surface area" or funInput == "sa":
            surarea()
        elif funInput == "fahrenheit" or funInput == "fah":
            fahrenheit()
        elif funInput == "celsius" or funInput == "cel":
            celsius()
        elif funInput == "volume" or funInput == "vol":
            volume()
        elif funInput == "end" or funInput == "stop":
            running = False
        else:                   #if the input does not match any valid strings it gets sent to here
            print("\n\nUnfortunatly this is not a valid option or not implemented yet, please let the author know.\n\n")
    
#start of the main loop and non function based code		
startup()
print()
print("Thanks for using my calculator. Enjoy your day!")




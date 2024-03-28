#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#import required modules

import math
import random

#define functions
def help():
    print("AYYY I'm helping ere")
    
def clearline(n):       
    """This is the clear line function
    
    This function takes an integer and prints that many blank lines in the 
    window.
    """
    for x in range(n):  
        print()

def surarea():
    """
    This is the function for calculating surface area. 
    This function will calculate the surface area of a handful of different 
    objects. It uses the above function to help readability for code.
    """
    clearline(3)
    print("Here is a list of currently coded shapes.\n"
          "'rectangle' 'circle' 'triangle'...")
    clearline(3) 
    shape = input("What is the shape you are trying to calculate?   ")
    clearline(3)

    if shape == "rectangle" or shape == "rec": 
        l = float(input("What is the length?   "))
        h = float(input("What is the height?   "))
        sa = l*h
        clearline(3)
        print("The surface area of the rectangle is " 
              + str(sa) 
              + " units squared.")
        clearline(3)

    elif shape == "circle" or shape =="cic":
        pi = math.pi
        r = float(input("What is the radius of the circle?   "))
        sa = pi*(r**2)
        clearline(3)
        print("The surface area of the circle is " 
              + str(sa) 
              + " units squared.")
        clearline(3)

    elif shape == "triangle":
        b = float(input("What is the base of the triangle?   "))
        h = float(input("What is the height of the triangle?   "))
        a = b*h/2
        clearline(3)
        print("The surface area of the triangle is "
              + str(a) 
              + " units squared.")
        clearline(3) 
 
    else:
        clearline(3)
        print("This shape is not added yet please let the author know.")
        clearline(3)
        return

def percent():
    clearline(3)
    print("This works by taking a first number which is the "
          "position you are at,\n"
          "and a second number which is the total amount of places.")
    clearline(3)
    print("For example if you entered the numbers 5 and 15 you would"
          "be shown that \n"
          "you are 33 percent through and the ratio is 5/15.")
    clearline(3) 
    x = float(input("What is the number for the current positon?   "))
    y = float(input("What is the number for the total?   "))
    z = x*100/y
    clearline(3)
    print("You are currently "
          +str(z)
          + " percent through.\nThe ratio is " 
          +str(x)
          + "/" 
          +str(y)
          + ".")
          clearline(3)
    return

def volume():
    clearline(3)
    print("Here are a list of currently coded shapes.\n'cube'")
    clearline(3)
    shape = input("What is the shape you are trying to calculate?   ")
    if shape == "cube":
        l = float(input("What is your side length?   "))
        v = l**3
        clearline(3)
        print("The volume of this cube is " + str(v) +	 " units.")
        clearline(3)
 
    else:
        clearline(3)
        print("Not a valid option")
        clearline(3)

def fahrenheit():
    cel = float(input("What is the current degrees Celsius?   "))
    fah = (cel*9/5)+32
    clearline(3)
    print("It is currently "+str(fah)+" degrees Fahrenheit.")
    clearline(3)

def celsius():
    fah = float(input("What is the current degrees Fahrenheit?   "))
     #gets current teperature and sets in be an integer
    
    cel = (fah-32)*5/9 
    #formula to calculate celcius from fahrenheit

    clearline(3)
    print("It is currently "+str(cel)+" degrees Celsius.")
    #prints the string with the interjection of the output variable as a string
    clearline(3)

def fractodec(): #not an easy formula. 
    print ("not yet implemented")

def startup(running):

    """
    Here lies the main menu
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
          
    while running == True:
        clearline(3)
        
        #asking for input
        funInput1 = input("What would you like to do?   ") 
        
        #forcing the inputed string to become all lowercase
        funInput = funInput1.lower()
        
        #check if input is equal to the string if so run the function
        if funInput == "percentage" or funInput == "per":
            #run the function
            percent()
        
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
        else:
        #if the input does not match any valid strings it gets sent to here
            clearline(3)
            print("Unfortunatly this is not a valid option or not implemented yet, please let the author know.")
            clearline(3)
    
#start of the main loop and non function based code		
startup(True)
print()
print("Thanks for using my calculator. Enjoy your day!")
print("Written and maintained by Brady Clark-Doherty.")



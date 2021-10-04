# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
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

<<<<<<< HEAD
def surarea():
	"""This is the function for calculating surface area. 
    
    """
    print("\n\n\nHere is a list of currently coded shapes.")
    print("'rectangle' 'circle' 'triangle'. \n\n\")
    shape = input("What is the shape you are trying to calculate?   ")
    if shape == "rectangle": 
        l = int(input("What is the length?   "))                                                    #asks for the length of the rectangle
        h = int(input("What is the height?   "))                                                    #asks for the height of the rectangle
        sa = l*h                                                                                    #surface area equals length times height
        print("\n\nThe surface area of the rectangle is " + str(sa) + " units squared.\n\n")        #print the answer in a formatted text
    elif shape == "circle":                                                                         #checks if the shape is a circle
        pi = math.pi                                                                                #this is pi 
        r = int(input("What is the radius of the circle?   "))                                      #asks for the radius of the circle
        sa = pi*(r**2)                                                                              #surface area equals pi x (radius squared)
        print("\n\nThe surface area of the circle is " + str(sa) + " units squared.\n\n")           #print the answer in formatted text
    elif shape == "triangle":                                                                       #checks if the shape is a triangle
        b = int(input("What is the base of the triangle?   "))                                      #asks for the base of the triangle
        h = int(input("What is the height of the triangle?   "))                                    #asks for the height of the triangle
        a = b*h/2                                                                                   #area equals base times height divided by two
        print("\n\nThe surface area of the triangle is "+ str(a) +" units squared.\n\n")            #print the answer in formatted text
    else:                                                                                           #if the response didnt match any of the answers do the following
        print("\n\nThis shape is not added yet please let the author know.\n\n")                    #Invalid text text
        return
=======
def surarea():#this is the function for calculating surface area
	
	print("\n\n\nHere is a list of currently coded shapes.\n'rectangle' 'circle' 'triangle'\n\n\n") #this is a list of shapes that the program can calculate surface area for
    shape = input("What is the shape you are trying to calculate?   ")                              #asks for a shape to calculate
	if shape == "rectangle":                                                                        #checks if the shape is a rectangle  
	    l = int(input("What is the length?   "))                                                    #asks for the length of the rectangle
	    h = int(input("What is the height?   "))                                                    #asks for the height of the rectangle
	    sa = l*h                                                                                    #surface area equals length times height
		print("\n\nThe surface area of the rectangle is " + str(sa) + " units squared.\n\n")        #print the answer in a formatted text
	elif shape == "circle":                                                                         #checks if the shape is a circle
	    pi = math.pi                                                                                #this is pi 
	    r = int(input("What is the radius of the circle?   "))                                      #asks for the radius of the circle
	    sa = pi*(r**2)                                                                              #surface area equals pi x (radius squared)
		print("\n\nThe surface area of the circle is " + str(sa) + " units squared.\n\n")           #print the answer in formatted text
	elif shape == "triangle":                                                                       #checks if the shape is a triangle
	    b = int(input("What is the base of the triangle?   "))                                      #asks for the base of the triangle
	    h = int(input("What is the height of the triangle?   "))                                    #asks for the height of the triangle
	    a = b*h/2                                                                                   #area equals base times height divided by two
		print("\n\nThe surface area of the triangle is "+ str(a) +" units squared.\n\n")            #print the answer in formatted text
	else:                                                                                           #if the response didnt match any of the answers do the following
		print("\n\nThis shape is not added yet please let the author know.\n\n")                    #Invalid text text
		return
>>>>>>> 7ef208246e2401798036a1ac749e769ca6bf12e8

def percent():
    print("\n\n\nThis works by taking a first number which is the position you are at and a second number which is the total amount of places.\nFor example if you entered the numbers 5 and 15 you would be shown that you are 33 percent through and the ratio is 5/15.\n\n\n")
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
    clearline(10) #this is a clear line fuction that takes an argument (n) and prints that many blank lines
    print("Welcome to the Useful Calculator.\nWith this program you will be able to calculate many different formulas to find your missing number.\n\n\n\nType 'surface area' to calcualte the surface area of different objects.\nType 'volume' to calculate the volume of different objects.\nType 'percentage' to calculate the percentage of the numbers you have.\nType 'fahrenheit' to calculate Fahrenheit from Celsius.\nType 'celsius' to calculate Celsius from Fahrenheit.\nType 'end' to quit the calculator and retrieve the save data.\n")
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



def test():
    

#import required modules

import math
import random

# define global variables
running = False # this variable is for the starting loop


#define functions
def clearline(n):
    for x in range(n):  #for every number between zero and the integer provided when calling the function
        print()         #print an empty line 

def surarea():#this is the function for calculating surface area
	
	print("/n Here is a list of currently coded shapes. 'rectangle' 'circle' 'triangle'") #this is a list of shapes that the program can calculate surface area for
	clearline(3)                                                                          #this is a clearline 3
	shape = input("What is the shape you are trying to calculate?   ")                    #asks for a shape to calculate
	print()
	if shape == "rectangle":                                                              #checks if the shape is a rectangle  
		l = int(input("What is the length?   "))                                          #asks for the length of the rectangle
		h = int(input("What is the height?   "))                                          #asks for the height of the rectangle
		sa = str(l*h)                                                                     #how would one describe this line of code
		
		print("\n\nThe surface area of the rectangle is " + sa + " units squared.")
	
	elif shape == "circle":
		pi = 3.1415926
		r = int(input("What is the radius of the circle?   "))
		sa = pi*r**2
		print()
		print("The surface area of the circle is " + sa + " units squared.")
		
	elif shape == "triangle":
		b = int(input("What is the base of the triangle?   "))
		h = int(input("What is the height of the triangle?   "))
		a = b*h/2
		print()
		print("The surface area of the triangle is "+ a +" units squared.")
		
	else:
		print("This shape is not added yet please let the author know.")
		return

def percent():
	x = int(input("What is the number for the current positon?   "))
	y = int(input("What is the number for the total?   "))
	z = x*100/y
	print()
	print("You are currently " +str(z)+" percent through.")
	print()
	print("The ratio is "+str(x)+"/"+str(y)+".")
	return

def volume():
	shape = input("What is the shape you are trying to calculate?   ")
	
	
	
	
	if shape == "cube":
		print()
		l = int(input("What is your side length?   "))
		v = l**3
		print()
		print("The volume of this cube is " + str(v) +	 " units.")
		print()
	
	else:
		print()
		print("Not a valid option")


def fahrenheit():
	cel = int(input("What is the current degrees Celsius?   "))#gets current temperature and sets in to be an integer
	fah = (cel*9/5)+32              #formula for calculating fahrenheit from celsius
	print()
	print("It is currently "+str(fah)+" degrees Fahrenheit")  #prints the string with the interrjection of the output variable as a string
	return

def celsius():
	fah = int(input("What is the current degrees Fahrenheit?   ")) #gets current teperature and sets in be an integer
	cel = (fah-32)*5/9 #formula to calculate celcius from fahrenheit
	print()
	print("It is currently "+str(cel)+" degrees Celsius") #prints the string with the interjection of the output variable as a string
	return

def fractodec(): #not an easy formula. 
	print ("not yet implemented")
	return

def startup():
	clearline(10) #this is a clear line fuction that takes an argument (n) and prints that many blank lines
	print("Welcome to the Useful Calculator.")
	print("With this program you will be able to calculate many different formulas to find your missing number. What would you like to calculate?")
	clearline(3)
	print("Type 'surface area' to calcualte the surface area of different objects.")
	print()
	print("Type 'volume' to calculate the volume of different objects.")
	print()
	print(" Type 'percentage' to calculate the percentage of the numbers you have.")
	print()
	print("Type 'fahrenheit' to calculate Fahrenheit from Celsius")
	print()
	print("Type 'celsius' to calculate Celsius from Fahrenheit")
	clearline(3)
	
	funInput1 = input("What would you like to do?   ") #asking for input
	print()
	funInput = funInput1.lower() #forcing the inputed string to become all lowercase
	#the following if statement checks the given input against the available functions to be called.
	if funInput == "percentage" or "per": #check if input is equal to the string if so
		percent()             #run the function
	elif funInput == "surface area" or "sa":
		surarea()
	elif funInput == "fahrenheit" or "fah":
		fahrenheit()
	elif funInput == "celsius" or "cel":
		celsius()
	elif funInput == "volume" or "vol":
		volume()
	
		
		
	else:                   #if the input does not match any valid strings it gets sent to here
		print("Unfortunatly this is not a valid option or not implemented yet, please let the author know")
		clearline(10)
		
#start of the main loop and non function based code		

	

#startUp()
print()
print("Thanks for using my calculator. Enjoy your day!")

 #print("This \n is a \n new line test \n\n\n 3lines") #this is the working new line comment

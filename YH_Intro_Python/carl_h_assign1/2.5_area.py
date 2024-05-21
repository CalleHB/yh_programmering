#This method belongs to the mathematical module in Python
import math

#ask the user to imput a number of a radius.
radius_in = float(input("Input a number that you want the radiys of! Enter here: "))

#take the input from the user and multiply it with PI times 2 and round it of to 1 decimal
diameter = round(math.pi * radius_in ** 2 , 1)
#print answer to userconsol
print(diameter)
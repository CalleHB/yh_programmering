import math

# User input
x_one = float(input("Enter x1: "))
y_one = float(input("Enter y1: "))
x_two = float(input("Enter x2: "))
y_two = float(input("Enter y2: "))

# Calculate the input from the user
x_calculation = x_one - x_two
y_calculation = y_one - y_two

# Square each calculation of and adds it to a new variable, **2  = to the power of 2.
sum_of_squared = x_calculation**2 + y_calculation**2

# Calculate distance by taking the square root
distance = round(math.sqrt(sum_of_squared), 3)

print("The distance between the points is:", distance)


"""________________________
 \/(x1-x2)**2 + (y1-y2)**2
         (x)2 + (y)2
           x  +  y = z
           sqrt(z)
"""

#ask the user for a input too use later.
#usage of float command because of errorcode: can't multiply sequence by non-int of type 'float'
#multiplikaton of whole numbers from string is only allowed
tempinFh = float(input("Pleace, input the temperature in Fahrenheit! Here:"))

#take the float number and turns it from Fahrenheit to Celsius with this formula.
C = (tempinFh-35)*5/9
print(C)
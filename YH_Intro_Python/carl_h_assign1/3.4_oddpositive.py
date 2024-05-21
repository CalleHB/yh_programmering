#import the library for random so we can use it in our code.
import random

#generat a random number that we save to our variable.
randomnumber= (random.randint(-10,10))

#make a first if statment to cheak if the number is 0 or not.
if randomnumber == 0:
    print("The number", randomnumber, "is even and neither positive nor negative")
    
#if the number is't zero we check if it's negative or positiv and if its even or odd
if randomnumber <= 0:
    print("The number", randomnumber, "is negative")
    if randomnumber % 2 == 0:
        print("The number,", randomnumber, "is even")
    else:
        print("The number,", randomnumber, "is odd")
#if the number is positive, we cheak if its even or odd.
else:
    print("The number", randomnumber, "is positive")
    if randomnumber % 2 == 0:
        print("The number,", randomnumber, "is even")
    else:
        print("The number,", randomnumber, "is odd")
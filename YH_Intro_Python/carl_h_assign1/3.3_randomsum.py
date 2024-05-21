#import the library for random so we can use it in our code.
import random

#create an empty list to put our randoms number in.
sumofnumbers = []

#make a for loop that loops throue the code below 5 times to get random numbers and adds then to the list. in this case i = 5(we want the code below to run 5 times)
for i in range(5):
    sumofnumbers.append(random.randint(1,100))

#print out our list without square brackets using *(unpack operator?) before our variable.
print(*sumofnumbers)

#make a variable to save our counted lits to, we use sum to combinde all number in our list we named sumofnumber.
total = sum(sumofnumbers)

#print the total number of the list.
print("The total of our random numbers are:", total)

import random
#our variables
sumofnumbers = random.sample(range(1,36),7)#this way we get 7 unik numbers.

#print output to the user
print ("The lotto numbers for this we are:")
for num in sumofnumbers:
    print(num, end=' ')
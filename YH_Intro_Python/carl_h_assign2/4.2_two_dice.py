import random
#our list and dictionary
sumofnumbers = []
frequency = {}

#for loop to get 10000 dice rolles with two dices.
for i in range(10000):
    sumofnumbers.append(random.randint(1,6) + random.randint(1,6))

#her i can to count the number to se if the number exist or if its missing from the dictionary
for num in sumofnumbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

#here i print a sorted and print out the frequency of the list with a for loop. 
for num, freq in sorted(frequency.items()):#go throu the dictionarys items in a sorted way.
    
    print (f"The number {num}, landed after 10000 rolles: {freq} times!")

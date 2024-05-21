import random

#get user input
user_input = int(input("Enter a positiv number! Enter here: "))

#check if input is right or not
if user_input <= 0:
    print(f"{user_input} is not a positiv number!")
    user_input = int(input("Enter a positiv number! Enter here: "))
#empty list
sumofnumbers = []

#generat a random number for every i in range from user input and we use append to put it into ouyr list.
for i in range(user_input):
    sumofnumbers.append(random.randint(1,100))

#variabels for the math we need to use
total = sum(sumofnumbers)# total sum of all item in list 
avg = round(total / user_input, 2)#generate the average value with 2 decimals
min_number = min(sumofnumbers)# the lowers value in the list
max_number = max(sumofnumbers)# the highest value in the list


#print all our variables 
print(f"Ur input of {user_input} generated the numbers:")
print(*sumofnumbers)
print(f"The avarege number is {avg}\nThe min number is {min_number}.\nThe max number is {max_number}.")


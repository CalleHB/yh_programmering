#import funktions
from stringfunctions import reverse
def listprint(a):
    for integer, number in enumerate(a): #will go throue the list and print ever number and posistion connected to that number.
        print(f"Integer {integer}: {number}")
        
#variabels
list_num = []
count = 0

#user input and saved to list
user_in = int(input("Add as many positiv numbers you want.\nTo end the loop add a negative number: "))
list_num.append(user_in)

#loop will continue until the user input a negativ number, takes user input, add 1 to how many input the user has made.
while user_in > 0:
    
    user_in = int(input("Add as many positiv numbers you want.\nTo end the loop add a negative number: "))
    list_num.append(user_in)
    count += 1

#call our funtion and print the result backwards.
listprint(list_num)
print(f"The number of positiv numbers are: {count} \n In reverse order:{reverse(list_num)}")


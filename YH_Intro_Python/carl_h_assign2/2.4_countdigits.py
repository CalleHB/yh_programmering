#declare variabels
zeros = 0
odds = 0
even = 0

#get user input
input_user = int(input("Enter a large positive number: "))

#loop througe the users input, convert it to a string, checks if its a 0,even or odd.
for i in str(input_user):
    if i == '0':
        zeros += 1
        
    elif int(i) % 2 == 0:
        even += 1

    else:
        odds += 1
        
#print output
print("We have",zeros ,"zeros,",even,"even numbers","and", odds, "odd numbers!!" )


#get user input
user_number = int(input("Write a number: "))

#here we test if the user can read or not.
if user_number <= 0:
    print("Invalid input")

#if they can read we start a for loop to add 2 ever time we loop to get tthe next odd number
else:
    
    #declare variabels
    sum = 1
    k = 0

    for i in range(1,user_number,2): #for loop that starts at 1 and end when it hits the users input, adds 2 ever run
        sum = sum + i #add i to sum everytime to get the next odd number
        if(sum >= user_number):#if sum get greater or equal to the users input we break
            k = i #k is now the number of odd loops we have made.
            break
    print("Smallest n is", k)
        
        
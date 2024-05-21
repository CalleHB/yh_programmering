#get user input
user_number = int(input("Write a number: "))

#here we test if the user can read or not.
if user_number <= 0:
    print("Invalid input")

#if they can we start a for loop to add 2 ever time we loop to get tthe next odd number
else:
    #declare variabels
    sum = 0
    k = 0
    
    #a while loop that will run as long as sum is lower then the users input
    while sum < user_number:
        k += 2 #add 2 to k
        sum += k #update sum with k 
    
    #remove 2 at the end, we went over the last turn in the while loop, fix for this?        
    k -= 2
    
    print(f"{k} is the largest k!")
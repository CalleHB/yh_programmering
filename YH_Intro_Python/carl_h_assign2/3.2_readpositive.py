#user input
user_input = int(input("Enter a odd and positiv number: "))

count_runs = 0

#while loop so that the number need to match our question
while user_input <= 0 or user_input % 2 == 0:    
    
    print("Thats not the right number!")
    user_input = int(input("Enter a odd and positiv number: "))
    count_runs += 1
    
    #if the input is correct we print out and exit
    if user_input >= 0 and not user_input % 2 == 0:
        print(f"Good work, {user_input} is right!")
    
    #to many tryes. exit 
    if count_runs >= 4:
        print("Thats five guesses, better luck next time!")
        break
        

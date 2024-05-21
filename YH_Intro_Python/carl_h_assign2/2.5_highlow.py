#generat a random number 1-100
import random
right_number = random.randint(1,100)

#get tha users input 
user_guess = int(input("Guess a number from 1-100 Enter here: "))
guess_count = 0

#while loop for guessing game 1-100, after 10 fails it exits
while user_guess != right_number:
    guess_count += 1
    
    #if the user guesses to low
    if user_guess < right_number:

        print("Wrong number guess agien!")
        print("The right nummber is higher!")
        user_guess = int(input("Guess a number from 1-100! Enter here: "))
        
    #if the user guesses to high
    else:
        print("Wrong number guess agien!")
        print("The right number is lower!")
        user_guess = int(input("Guess a number from 1-100! Enter here: "))
        
    #if the user guesses the right number
    if user_guess == right_number:
        print(f"{right_number}, is the right number! Great work and on only {guess_count} trys!")
        
    #if the user guesses to many time
    if guess_count == 10:
        print("This might not be your thing mate.")
        break

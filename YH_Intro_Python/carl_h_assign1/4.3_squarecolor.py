
#get input from user
square_to_check = input("Input a square letter a-h and number 1-8 for the square you want the color of: ")

#make two list with the letters of a chessboard
white_even = ["a","c","e","g",]
black_even = ["b","d","f","h",]

#here i check what letter and number the users want to check.
letter_to_check = square_to_check[0]
number_to_check = int(square_to_check[1])

#here i want to cross reference the list from 
if letter_to_check in white_even:
    if number_to_check % 2 == 0:
        print("The square,", square_to_check, "is White")
    else:
        print("The square,", square_to_check, "is Black")
    
if letter_to_check in black_even:
    if number_to_check % 2 == 0:
        print("The square,", square_to_check, "is Black")
    else:
        print("The square,", square_to_check, "is White")

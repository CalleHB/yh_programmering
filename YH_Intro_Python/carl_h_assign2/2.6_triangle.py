#get user input
user_input = int(input("Enter a positiv odd number! Enter here: "))

#check if input is right or not
if user_input % 2 == 0 or user_input <= 0:
    print(f"{user_input} is not a odd positiv number!")
    user_input = int(input("Enter a positiv odd number! Enter here: "))
#if the input is correct we start the script, https://stackoverflow.com/questions/64031535/printing-a-right-angle-and-isosceles-triangle
else:
    print("Right-angled triangle:")
    for i in range(user_input): #for the range in the number in user_input, Ex input = 3, range = 1,2,3
        
        print(' ' * i, '*' * (user_input - i)) #prints a * for ever i in user_input and decrease the range of user_input by 1 every turn.
    
        
    print("Isosceles triangle:")    
    for i in range(1, user_input+1, 2): #for the range in the number in user_input, starting att 1 and adding 2 every turn till we meet user_input
        
        #count the diffrens from user input and divides it by 2 to fint the center to start with. when we have found it we print a *
        print(" " * ((user_input -i) // 2), "*" * i)

#get 2 inputs from the user, first name and last name
first_name = input("Write your first name: ")
last_name = input ("write your last name: ")

#here we want to get the 3 first number in the lastname and attach it to our variable
lastname = last_name[0:3]

#print out the users input.
print("Your first name is: ", first_name)
print("Your first name is: ", last_name)

#print out the first names first letter and the variabel lastname containing only the first 3 letters.
print("Your short name is:",first_name[0] + "." + lastname)
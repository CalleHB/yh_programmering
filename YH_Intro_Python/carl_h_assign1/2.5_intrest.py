#get costumers initial savings, int before print to get integers numbers
Savings = int(input("How much do you intend to save? Input value here:"))

Percentage = int(input("How much intrest do you want:"))

#years = int(input("How meny years do you want to save? Enter years: "))

#this code takes the input from the user, 
#then takes that and multiply it with 9 then 5 and divides it by 100 to get the diffrens before adding it to the input number.
value = Savings*(1 + Percentage/100)**5

print(round(value))


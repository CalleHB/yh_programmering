#get input from user
price = float(input("Enter the price of your merchandise. Enter here: "))
payment = float(input("Enter the price of your payment. Enter here: "))

#get the change and round if of
change = round(payment - price) 

#make a list thet contains all our bills we have
bill = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Ur change is: ", change, "in the following bills:")

#here i want to loop through and try to find the bills that we can use as change
for i in bill:
    if change >= i: #if change is equal or greater then i(if there is any money left)
        newbills = change // i #Calculate how many bills in 'i' are needed
        print(f"{newbills}st: {i}kr")#uses f-strings så python bara kör ut allt som det står.str och int
        change %= i #update the current change whit what is left in change and then repeat.
        
    

seconds_input = int( input("Give a number of seconds! Enter Here: "))

seconds_for_loop = seconds_input

#takes the users input and test if it fits inside one hour(3600sec)
hours = seconds_for_loop // 3600

#Then we count the remaning seconds and update the variable 
seconds_for_loop %= 3600

#we take the remaning seconds and se how many minutes we can fit it in(60sec)
minutes = seconds_for_loop // 60

#Then we count the remaning seconds and update the variable
seconds_for_loop %= 60

#now we print the result that we get frm each count 
print("Your input:" + str(seconds_input) +" is> Hours: " + str(hours),"Minutes: " + str(minutes), "Seconds: " + str(seconds_for_loop))
#count for how many numbers we have prited
new_line = 0

#here i declear i wnat to use the range 100-201(+1 to end on 200)
for i in range(100,201):
    #controll if the number is divisible ty 4 or 5, but not both and print the number after each other. Adds 1 for each loop
    if (i % 4 == 0 or i % 5 == 0) and not (i % 4 == 0 and i % 5 == 0):
        print(i, end=' ')
        new_line += 1
        
        #when count is 10, we start at a new line and clear the counter
        if new_line == 10:
            print()
            new_line = 0
#deffine our numbers and save them to veriabels
print("Enter 3 numbers here:") 
A = int(input("A=")) 
B = int(input("B="))
C = int(input("C="))

#print out the numbers ur users put in.
print(f"Your numbers are: {A}, {B}, {C}")

#compare all the input to finde whitch one is largest.
#users if/else to compare all inputs
if A >= B:
    if A >= C:
        largest = A
    else:
        largest = C
#else if B is bigger then A we discard A because B is bigger then one of the nummbers and check it to the last one.
else:
    if B >= C:
        largest = B
    else:
        largest = C

#print out the largers number.
print("The largest nummer is:", largest)

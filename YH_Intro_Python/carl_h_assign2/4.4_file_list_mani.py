from list_funtions import *

listtest = random_list(5)

average(listtest)

print(only_odd(listtest))

print(to_string(listtest))

print(contains([1,2,3,4], 2, 3)) #True
print(contains([1,2,3,4], 2, 4)) #False

print(has_duplicates([1, 2, 3, 4, 5]))  #Felse
print(has_duplicates([1, 2, 3, 4, 1]))  #True
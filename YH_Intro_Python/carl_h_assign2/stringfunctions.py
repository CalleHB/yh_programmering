#our functions
#write the word as many time as n is.
def concat(s, n):
    return s * n
#counts the letter x is assigned
def count(s, x):
    return s.count(x)
#switch the word structure
def reverse(s):
    return s[::-1]
#Switches the first and last letter in a word
def first_last(s):
    return s[0], s[-1]
#count if there is absolutly 2 XX in the variable
def has_two_X(s):
     return s.count('X') == 2
#scans the word for more the one of the same letter in a word.
def has_duplicates(s):
    return len(set(s)) <len(s)

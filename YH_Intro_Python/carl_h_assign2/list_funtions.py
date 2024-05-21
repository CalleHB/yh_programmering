import random

def random_list (n):
        return [random.randint(1,100) for _ in range(n)]

def average(lst):
    sumoflst = sum(lst)
    numinlist = len(lst)
    avg = sumoflst / numinlist
    print ("Average:", avg)
    return avg

def only_odd(lst):
    odd_list = []
    for num in lst:
        if num % 2 != 0:
            odd_list.append(num)

    return odd_list
        
def to_string(lst):
    return '"[' + ', '.join(map(str, lst)) + ']"'

def contains(lst, a, b):
    for i in range(len(lst) - 1):
        if lst[i] == a and lst[i + 1] == b:
            return True
    return False

def has_duplicates(lst):
    return len(lst) != len(set(lst))


#a funtion thats returns the value * amount.
def get_number(a, b, c, d):
    return 1000*a + 100*b + 10*c + d


#skjut mig. Fattar inte denna jag fick ta hjälp av chat. Vi kanske kan diskutera fram ett svar som jag fattar vid redovisning.
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                if get_number(d, c, b, a) == 4 * get_number(a, b, c, d):
                    print(f"A = {a}, B = {b}, C = {c}, D = {d}")

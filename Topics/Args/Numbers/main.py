# put your python code here
def multiply(*nlist):
    total = 1
    for n in nlist:
        total *= int(n)
    return total

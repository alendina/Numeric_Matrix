# use the function blackbox(lst) that is already defined
a = [1, 2, 3]
b = blackbox(a)
a[0] = "00"
print('modifies' if a is b else 'new')

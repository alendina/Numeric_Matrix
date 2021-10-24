def multiply(a, b):

    if b <= 1:  # base case
        return a
    else:
        return a + multiply(a, b - 1)

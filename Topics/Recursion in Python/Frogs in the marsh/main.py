def number_of_frogs(year):
    if year <= 1:
        return 120
    else:
        return 2 * (number_of_frogs(year - 1) - 50)


# print(number_of_frogs(1))
# print(number_of_frogs(5))

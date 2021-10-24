def average_mark(*numbers):
    number_list = [x for x in numbers]
    return round(sum(number_list) / len(number_list), 1)

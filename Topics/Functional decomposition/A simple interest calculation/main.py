def calculate(amount, interest_rate, time):
    interest = float(amount) * float(interest_rate) * float(time) / 100
    total_sum = amount * (1 + interest_rate / 100 * time)
    return interest, total_sum


def print_result(interest, total_amount):
    print(f'The interest is: {round(interest, 1)}')
    print(f'The total amount is: {round(total_amount, 1)}')


# print_result(calculate(input(), input(), input()))


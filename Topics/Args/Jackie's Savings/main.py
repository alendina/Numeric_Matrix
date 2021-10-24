def final_deposit_amount(*interest, amount=1000):
    for i in interest:
        amount += amount / 100 * i
    return round(amount, 2)


# print(final_deposit_amount(1000))

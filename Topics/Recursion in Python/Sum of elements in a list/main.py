def list_sum(some_list):
    if some_list == []:
        return 0
    elif len(some_list) == 1:  # base case
        return some_list[0]
    else:
        t = some_list[0]
        del some_list[0]
        return t + list_sum(some_list)


# print(list_sum([int(x) for x in input().split()]))

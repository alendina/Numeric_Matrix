def last_indexof_max(numbers):
    index_max = 0
    for n in range(1,len(numbers)):
        if numbers[index_max] <= numbers[n]:
            index_max = n
    return index_max

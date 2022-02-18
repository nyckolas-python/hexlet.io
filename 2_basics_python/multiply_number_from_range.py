def multiply_number_from_range(start, finish):
    multi_sum = 1
    i = start
    while i <= finish:
        multi_sum = multi_sum * i
        i = i + 1
    return multi_sum
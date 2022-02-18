def join_numbers_from_range(start, finish):
    result = ''
    i = start
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result
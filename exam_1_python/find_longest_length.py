def find_longest_length(str):
    sub_str = ''
    max_length = 0
    for i in str:
        if i not in sub_str:
            sub_str += i
            # print(sub_str) вывод текущей подстроки
        else:
            max_length = max(max_length, len(sub_str))
            # print(max_length) хранение значения максимальной длины подстроки
            sub_str = sub_str[sub_str.index(i) + 1:] + i
    max_length = max(max_length, len(sub_str))
    return max_length
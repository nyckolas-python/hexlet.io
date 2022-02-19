def my_substr(string, value):
    new_string = ''
    lenth = len(string) - 1
    i = 0
    if value <= lenth:
        while i < value:
            new_string = new_string + string[i]
            i = i + 1
        return new_string
    return string
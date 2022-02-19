from hexlet.code_basics import to_upper_case


# BEGIN (write your solution here)
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == str.lower(char) or string[index] == str.upper(char):
            # Считаем только подходящие символы
            count = count + 1
        # Счётчик увеличивается в любом случае
        index = index + 1
    return count
# END
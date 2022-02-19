ЗаданиеФункция из теории учитывает регистр букв. То есть A и a с её точки зрения разные символы. Реализуйте вариант этой же функции, так чтобы регистр букв был не важен:


count_chars('HexlEt', 'e') # 2
count_chars('HexlEt', 'E') # 2

Решение учителя:


from hexlet.code_basics import to_upper_case


# BEGIN
def count_chars(string, char):
	index = 0
    count = 0
    while index < len(string):
        if to_upper_case(string[index]) == to_upper_case(char):
            count = count + 1
    index = index + 1
    return count
# END

Моё решение:


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
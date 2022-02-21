ЗаданиеРеализуйте функцию does_contain(), которая проверяет с учётом регистра, содержит ли строка указанную букву (в этот раз не пользуйтесь оператором in!). Функция принимает два параметра:
	* Строка
	* Буква для поиска

Решение учителя:


def does_contain(string, char):
	index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False

Моё решение:


def does_contain(text, symbol):
	i = 0
    while i < len(text):
        if text[i] == symbol:
            return True
        i += 1
    return False
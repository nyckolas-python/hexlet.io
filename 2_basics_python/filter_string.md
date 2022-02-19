ЗаданиеРеализуйте функцию filter_string(), принимающую на вход строку и символ, и возвращающую новую строку, в которой удален переданный символ во всех его позициях.

Решение учителя:


def filter_string(text, char):
	index = 0
    result = ''
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result += current_char
        index += 1
    return result

Моё решение:


def filter_string(text, symbol):
	string_new = ''
    i = 0
    while i < len(text):
        if text[i] != symbol:
            string_new += text[i]
        i += 1
    return string_new
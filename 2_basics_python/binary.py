def binary(number):
    result = ''
    modulo = 0
    if number > 0:
        while number != 0:
            if number > 0:
                modulo = number % 2
                result = result + str(modulo)
                number = number // 2
            else: result = '0'
        return result
    elif number == 0:
        return str(number)
    else: return 'ошибка'
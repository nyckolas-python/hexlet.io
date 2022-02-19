Задание

Реализуйте функцию print_name_by_symbol(), которая печатает переданное слово посимвольно, как в примере из теории, но делает это в обратном порядке.


name = 'Arya'

print_name_by_symbol(name)
# => 'a'
# => 'y'
# => 'r'
# => 'A'

Моё решение:


def print_name_by_symbol(name):
	i = len(name) - 1
    while i >= 0:
        print(name[i])
        i = i - 1
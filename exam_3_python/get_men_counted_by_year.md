Реализуйте функцию get_men_counted_by_year(), которая принимает на вход список пользователей и возвращает словарь, в котором ключ — это год рождения, а значение — количество мужчин, родившихся в этот год.
```
from solution import get_men_counted_by_year
users = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]
get_men_counted_by_year(users)
# {1973: 3, 1963: 1, 1980: 2, 2012: 1, 1999: 1}
```
### Подсказки
Для решения можете использовать встроенный инструмент Counter.
Для работы с датами пригодится модуль datetime.
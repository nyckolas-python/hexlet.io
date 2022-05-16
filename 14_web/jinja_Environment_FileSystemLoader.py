from jinja2 import Environment, FileSystemLoader

'''
https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment

https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.FileSystemLoader
Загрузчики:

PackageLoader - для загрузки пакетов из шаблонов
DictLoader - для загрузки пакетов из словаря
FunctionLoader - для загрузки пакетов на основе фунции
PrefixLoader - загрузчик, использующий словарь для построения подкаталогов 
ChiceLoader - загрузчик, содержащий список других загрухчиков(если один не сработает,
выбирает следующий и т.д.)
ModuleLoader - загрузчик для скомпилированных шаблонов 
'''

persons = [
	{'name': 'Adam', 'age': 37, 'weight': 74},
	{'name': 'Nyckolas', 'age': 32, 'weight': 64},
	{'name': 'Michel', 'age': 42, 'weight': 84},
	{'name': 'Clarck', 'age': 47, 'weight': 94}
]

file_loader = FileSystemLoader('14_web/templates/')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users = persons)

print(msg)
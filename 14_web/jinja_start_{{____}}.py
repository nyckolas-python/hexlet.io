from jinja2 import Template
### Использование скобок {{}} в шаблонах Jinja

'''
class Person:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

per = Person('Nyckolas', 32)
'''
per = {'name': "Nyckolas", 'age': 32}


tm = Template('Привет, меня зовут {{ p.name.upper() }}!\nМне уже {{ p.age*2 }} года.')
msg = tm.render(p = per)

print(msg)
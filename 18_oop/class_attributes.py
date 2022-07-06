# Атрибуты класса

class Person:
	name = 'Mykola'
	age = 32
	
# Магический метод, выводит mappingproxy - словарь совсеми доступными методами.
print(Person.__dict__)

# Доступ к атрибутам
print(getattr(Person,'name', 'Ivan'))

# Изминение атрибутов
Person.name = 'Misha'
print(Person.name)

# Добавление/изминение новых атрибутов возможно двумя способами
Person.new = [1, 2, 3, 4]
print(Person.new) # [1, 2, 3, 4]
setattr(Person, 'new', [1, 2, 3, 4, 5])
print(Person.__dict__)
# mappingproxy({'__module__': '__main__',
# 				'name': 'Mykola', 'age': 32,
# 				'__dict__': <attribute '__dict__' of 'Person' objects>,
# 				'__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None,
# 				'new': [1, 2, 3, 4, 5]})

# Удаление атрибутов, тоже два варианта
del Person.new
delattr(Person, 'new')

# Вызов экземпляра класа
Person()

# Результат вызова экземпляра, можно присваивать переменным
a = Person()
b = Person()

# Изминение класса привидёт к изминению всех экземпляров класса
Person.new = [1, 2, 3, 4]
Person.new2 = {1, 2, 3, 4}

print(a.new) # [1, 2, 3, 4]
print(b.new2) # {1, 2, 3, 4}

# Но создание нового атрибута в отдельного экземпляра класа, не коснется всех экземпляров
a.new3 = '1, 2, 3, 4'
print(a.new3) # '1, 2, 3, 4'
print(a.new2) # {1, 2, 3, 4}
print(a.new1) # [1, 2, 3, 4]
print(getattr(b, 'new3', False)) # False
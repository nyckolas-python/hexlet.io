# Атрибуты экземпляра класса

class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a2 = Car()
a1.seat = 4
print(a1.__dict__) # {'seat': 4}
a1.model = 'Peugeot'
# Сначала идёт поиск в пространстве имен экземпляра класса, потом у самого класса.
print(a1.model) # 'Peugeot'
print(a1.__dict__) # {'seat': 4, 'model': 'Peugeot'}
print(a2.__dict__) # {}
print(Car.__dict__)
# mappingproxy({'__module__': '__main__',
# 'model': 'BMW', 'engine': 1.6,
# '__dict__': <attribute '__dict__' of 'Car' objects>,
# '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
# Если удалить атрибут экземпларя класса, то будет выводится атрибут самого класса
del a1.model
print(a1.model) # 'BMW'
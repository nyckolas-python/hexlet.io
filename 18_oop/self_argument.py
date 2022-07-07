#!/usr/bin/env python3

# аргумент self и магический метод __init__

from math import sqrt


class Cat:
    breed = 'pers'
    
    def hello(*args):
        print(f'Привет от кошки, ', args[0], '\nМяяяууу!')

    def show_breed(instance):
        print(f'My breed is {instance.breed}')

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'My name is {instance.name}')
        else:
            print('noting')
    
    def set_value_non_correrct(koshka, value):
        koshka.name = value
   
	# * Что такое self в классах?
	# self в классах - это общепринятое название ПЕРВОГО ОБЯЗАТЕЛЬНОГО аргумента метода,
	# в который всегда передается ссылка на сам объект у которого будет вызван метод.
	# Название может быть любым, но это не будет соответствовать PEP (стандарт написание кода)
	# Поэтому провально указывать первый аргумент у метода self
	
	# __init__ - магический, срабатывает сразу после создания объекта экземпляра класса, без его вызова.
 	# ОН используется для инициализации свих АТРИБУТОВ для каждого экземпляра класса.
  	# Обычно название аргументов метода совпадают с АТРИБУТАМИ, для понимания кода.

    def __init__(self, name, breed = 'pers' , age = 1, color = 'white'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

# В данном класе мы реализуем принцып DRY Dont repeat yoursefl. Так как основная ф-ция move_to
# мы использовали её для других методов передавая нужные аргументы.
 
class Point:
    
    list_points = []
    
    def __init__(self, coord_x=0, coord_y=0):
        #self.x = coord_x
        #self.y = coord_y
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)
    
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def go_home(self):
        #self.x = 0
        #self.y = 0
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')
        
    def calc_distace(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Точка")
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)
           
def test():
	p1 = Point(3, 4)
	p2 = Point(-54, 32)
	print(p1.x, p1.y)
	print(p2.x, p2.y)
	p1.print_point()
	#p1.calc_distace(90) # raise ValueError("Аргумент должен принадлежать классу Точка")
	print(p1.calc_distace(p2))
	print(f"Это список объектов класа Point: {Point.list_points}")
	print(f"В списке list_points в объекта {Point.list_points[1]} можем использовать \
    \nатрибуты  координат: {Point.list_points[1].x, Point.list_points[1].y}")
 
	Point.list_points[1].print_point() # Точка с координатами (-54, 32)

if __name__ == '__main__':
	test()
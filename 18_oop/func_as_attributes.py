# Функция как атрибут класса

class Car:
    model = 'BMW'
    engine = 1.6
    
    @staticmethod
    def drive():
        print("Let's go")
        
a = Car()
# При обращении к имени атрибуту-функции без вызова
# В самом классе выводит <function> а в экземпляре класса получаем <bound method>
print(Car.drive) # <function Car.drive at 0x7efffdf72a60>
print(a.drive) # <bound method Car.drive of <__main__.Car object at 0x7efffe8cca60>>
# При вызове атрибута-функции
# к самому классу ф-ция выполняется
# к экземпляру класса ф-ция НЕ выполняется, ловим ошибку TypeError
print(Car.drive()) # Let's go
print(a.drive()) # TypeError: drive() takes 0 positional arguments but 1 was given

# После добавления декоратора @staticmethod ф-ция отрабатывает даже при обращении к экземпляру
#!/usr/bin/env python3

# Public, Protected and Private method and attr
# Protected - название метода или атрибута начинается с _single_underscored
# Protected доступны для вызова из вне, но существует соглашение на уровне разработчиков 
# что их не стоит испольовать вне класса.

# Private - название метода или атрибута начинается с __double_underscored
# можно использовать внутри класса для методов, из вне прямого доступа нет.
# Из вне Python искажает название защищенный атрибутов, но если знаешь название класса,
# то можно к ним получить доступ по шаблону <object_name>._<class_name>__<attr_name>

class BankAccount:
    
	def __init__(self, name, balance, passport) -> None:
		self.__name = name
		self.__balance = balance
		self.__passport = passport
	
	# def print_public_data(self):
	# 	print(self.name, self.balance, self.passport)
 
	# Protected - название метода или атрибута начинается с _single_underscored
	def print_protected_data(self):
		print(self._name, self._balance, self._passport)

	# Private - название метода или атрибута начинается с __double_underscored
	# можно использовать внутри класса для методов, из вне прямого доступа нет.
	def print_private_data(self):
		print(self.__name, self.__balance, self.__passport)
  
def test():
    account1 = BankAccount('Mykola', 100500, 123456)
    account1.print_private_data() # Mykola 100500 123456
    
    # Python искажает название защищенный атрибутов, но если знаешь название класса, то можно 
    # к ним получить доступ по шаблону <object_name>._<class_name>__<attr_name>    
    print(account1._BankAccount__balance) # 100500
    print(account1._BankAccount__passport) # 123456
    # но напрямую доступа к атрибуту нет!
    print(account1.__name) # AttributeError: 'BankAccount' object has no attribute '__name'
  
if __name__ == '__main__':
	test()
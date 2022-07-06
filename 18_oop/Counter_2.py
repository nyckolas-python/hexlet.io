#!/usr/bin/env python3
class Counter:
# метод __init__ ("dunder-init", "дандер инит"). 
# Этот метод отвечает за инициализацию экземпляров класса после их создания.
	def __init__(self, value=0) -> int:
		self.value = value
# Именно через аргумент self метод получает доступ к атрибутам связанного объекта 
# (и его класса, конечно же).
# Методы inc, dec возращают новые экземпляры класса Counter
	def inc(self, delta=1):
		sf = self.value
		return Counter(sf + delta if sf + delta >= 0 else 0)
	
	def dec(self, delta=1):
		sf = self.value
		return Counter(sf - delta if sf - delta >= 0 else 0)

def test():
	c = Counter()
	print(c.inc().inc(5).dec(2).value) # 4
	d = c.inc(100)
	print(d.dec().value) # 99
	forty_two = Counter(42)
	print(forty_two.value) # 42

if __name__ == '__main__':
	test()
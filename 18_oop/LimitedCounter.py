#!/usr/bin/env python3
from Counter import Counter
# класс для теста
# class Counter:
# 	def __init__(self):
# 		self.value = 0

# 	def inc(self):
# 		self.value += 1

# 	def dec(self):
# 		self.value -= 1

           


class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
	def dec(self):
		pass

class DoubleCounter(Counter):
	def inc(self):
		super().inc()
		super().inc()

class LimitedCounter(Counter):
	def __init__(self, limit=10, value=0):
		self.limit = limit
		self.value = value

	def inc(self):
		if 0 <= super().inc() <= self.limit:
			super().inc()
		else:
			self.value = self.limit
		return self.value

	def dec(self):
		super().dec()

def test():
	mary = Cat()
	mary.show_name()
	mary.show_breed()
	mary.set_value('MARY')
	mary.show_name()
	print(mary.name)

if __name__ == '__main__':
	test()
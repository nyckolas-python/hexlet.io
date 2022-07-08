#!/usr/bin/env python3
#
# Наследование классов для теста
class Counter:
	def __init__(self):
		self.value = 0

	def inc(self, delta=1):
		self.value += delta

	def dec(self, delta=1):
		self.value -= delta

class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
	def dec(self):
		pass

class DoubleCounter(Counter):
	def inc(self):
		super().inc()
		super().inc()

class LimitedCounter(Counter):
	def __init__(self, limit=10):
		self.limit = limit
		self.value = 0

	def inc(self, delta=1):
		if self.value + delta < 0:
			self.value = 0
		elif self.value + delta <= self.limit:
			super().inc(delta)
		else:
			self.value = self.limit
		return self.value

	def dec(self, delta=1):
		self.inc(delta*-1)

def test():
	a = LimitedCounter()
	print(dir(a))
	a.inc(7)
	a.dec(6)
	a.dec(2)
	print(a.value) # 0
	a.inc(12)
	print(a.value) # 10
 
	

if __name__ == '__main__':
	test()
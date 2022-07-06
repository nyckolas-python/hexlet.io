#!/usr/bin/env python3

# класс для теста
class Counter:
	def __init__(self):
		self.value = 0

	def inc(self):
		self.value += 1

	def dec(self):
		self.value -= 1

class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
	def dec(self):
		pass

class DoubleCounter(Counter):
	def inc(self):
		super().inc()
		super().inc()


def test():
	n = NonDecreasingCounter()
	n.inc()
	n.inc()
	print(n.value)
	n.dec()
	print(n.value)


if __name__ == '__main__':
	test()

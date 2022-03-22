def update(d, **kwargs):
	c = {}
	c = d.copy()
	c.update(kwargs)
	return c

# Test Program
d = {'a': 1, 'b': True}
print(update(d, a=2, b=False, c=None)) # {'a': 2, 'b': False, 'c': None}
print(update(d) == {'a': 1, 'b': True}) # True
print(update(d) is d) # False
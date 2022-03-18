def apply_diff(target, diff):
	target.update(diff['add'])
	target.difference_update(diff['remove'])
	return target

# Test Progmram
target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target) # {'c', 'b'}
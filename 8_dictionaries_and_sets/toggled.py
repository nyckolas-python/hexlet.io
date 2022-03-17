def toggled(s, f):
	new_f = f.copy()
	new_f.discard(s) if s in new_f else new_f.add(s)
	return new_f

# Test programm
READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags) # False
print(READ_ONLY in new_flags) # True
print(flags) # set()
print(new_flags) # {'read_only'}
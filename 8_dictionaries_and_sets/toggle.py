def toggle(s, f):
	f.discard(s) if s in f else f.add(s)

# Test programm
READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)


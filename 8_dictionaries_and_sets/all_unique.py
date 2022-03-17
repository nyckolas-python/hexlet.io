def all_unique(iter):
	return print(len(set(iter)) == len(iter))

# Test programm
all_unique('cat')
all_unique([1, 2, 3])
all_unique([1, 2, 1])
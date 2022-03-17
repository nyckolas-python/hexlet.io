from collections import defaultdict

def collect_indexes(s):
	d = defaultdict(list)
	i = 0
	for k in s:
		d[k].append(i)
		i += 1
	return dict(d)

# Test programm
d = collect_indexes('hello')
print(d['h'])
print(d['e'])
print(d['l'])
def make_module(step=1):
	mdict = {
		'inc': lambda x: x + step,
		'dec': lambda x: x - step
		}
	return mdict

# Test Program
p = make_module()
print(p['inc'](10)) # 11
print(p['dec'](20)) # 19

p2 = make_module(step=2)
print(p2['inc'](1)) # 3
def conv(n, ri = 10, ro = 16): # Ф-ция конвертации (от 2 до 36) и наоборот (от 36 до 2)
	digs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	acc = 0
	res = ""
	if n in {0, '00', '0'}:
		res = '00'		
	for a in str(n).upper():
		k = digs.find(a)
		acc = acc * ri + k		
	while acc > 0:
		k = acc % ro
		res = digs[k] + res
		acc = acc // ro
	return res

def rgb2hex(r,g,b):
	hex = conv(r) + conv(g) + conv(b) # По умолчания конвертирует с 10 в 16
	print(hex)
	return hex

def hex2rgb(line):
	rgb = {}
	rgb['r'] = int(conv(line[1:3],16,10)) # первый аргумент срез строки,
	rgb['g'] = int(conv(line[3:5],16,10)) # 2 и 3 аргумент с какой в какую кодировку
	rgb['b'] = int(conv(line[5:],16,10)) # оборачиваем в int() если хотим число, а не строку
	print(rgb)
	return rgb


# Test Program

rgb2hex(36, 171, 0);
# '#24AB00'
rgb2hex(r=36, g=171, b=0)
# '#24AB00'
hex2rgb('#24ab00')
# {'r': 36, 'g': 171, 'b': 0}
def to_roman(num):
	roman = { # Dictionary of roman numbers
		1000: 'M',
		900: 'CM',
		500: 'D',
		400: 'CD',
		100: 'C',
		90: 'XC',
		50: 'L',
		40: 'XL',
		10: 'X',
		9: 'IX',
		5: 'V',
		4: 'IV',
		1: 'I'
		}
	result = ''
	if num < 4000:	
		for i in roman:
			result += num // i * roman[i]
			num %= i
		return result
		print(result)
	else:
		return False
		print(False)

def to_arabic(txt):
	txt = txt.upper()
	try:
		res = roman.fromRoman(txt)
		print(res)
	except roman.InvalidRomanNumeralError:
		print('Вы указали НЕ Римское число!')
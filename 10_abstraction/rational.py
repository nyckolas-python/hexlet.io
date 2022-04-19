from math import gcd

def make_rational(numer, denom):	
	nod = gcd(numer,denom)
	numer = int(numer/nod)
	denom = int(denom/nod)
	return "{}/{}".format(numer, denom)

def get_numer(rational):
	numer, _ = rational.split('/')
	return int(numer)

def get_denom(rational):
	_, denom = rational.split('/')
	return int(denom)

def add(ratio1,ratio2):
	numer = get_numer(ratio1)*get_denom(ratio2) + get_numer(ratio2)*get_denom(ratio1)
	denom = get_denom(ratio1)*get_denom(ratio2)
	return make_rational(numer,denom)

def sub(ratio1,ratio2):
	numer = get_numer(ratio1)*get_denom(ratio2) - get_numer(ratio2)*get_denom(ratio1)
	denom = get_denom(ratio1)*get_denom(ratio2)
	return make_rational(numer,denom)

rat1 = make_rational(3, 9)
print(get_numer(rat1)) # 1
print(get_denom(rat1)) # 3

rat2 = make_rational(10, 3)

rat3 = add(rat1,rat2)
print(rat3) # 11/3

rat4 = sub(rat1,rat2)
print(rat4) # -3/1
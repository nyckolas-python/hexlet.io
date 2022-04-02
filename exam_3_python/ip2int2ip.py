from ipaddress import IPv4Address


def ip2int(line):
	# First Method
	adr = IPv4Address(line)
	print(int(adr))

	# Second Method
	a,b,c,d = line.split('.')
	x = int(a) * 256**3 + int(b) * 256**2 + int(c) * 256 + int(d)	
	if x == int(adr):
		print(x)
		return x

def int2ip(ipnum):
	# First Method
	line = str(IPv4Address(ipnum))
	print(line)

	#Second Method
	a = ipnum//256**3
	b = (ipnum - (a*256**3))//256**2
	c = (ipnum - a*256**3 - b*256**2)//256
	d = (ipnum - a*256**3 - b*256**2 - c*256)
	res_line = f'{a}.{b}.{c}.{d}'
	if res_line == line:
		print(res_line)
		return line

# Test Program

ip2int('128.32.10.1')
# 2149583361
ip2int('0.0.0.0')
# 0
ip2int('255.255.255.255')
# 4294967295

int2ip(2149583361)
# '128.32.10.1'
int2ip(0)
# '0.0.0.0'
int2ip(4294967295)
# '255.255.255.255'
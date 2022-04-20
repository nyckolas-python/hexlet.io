from urllib.parse import parse_qsl, urlencode, urlparse
import url


def make(url):
	data_url = urlparse(url)
	return data_url

def get_scheme(data):
	print(data.scheme)
	return data.scheme

def set_scheme(data, scheme):
	#print(data._replace(scheme = scheme))
	return data._replace(scheme = scheme)

def get_host(data):
	print(data.host)
	return data.host

def set_host(data, host):
	#print(data._replace(host = host))
	return data._replace(host = host)
	
def get_path(data):
	print(data.path)
	return data.rath

def set_path(data, path):
	#print(data._replace(path = path))
	return data._replace(path = path)

def get_query_param(data, param_name, default = None):
	queryes = dict(parse_qsl(data.query))
	param_value = queryes.get(param_name, default)
	print(param_value)
	return param_value

def set_query_param(data, key, value):
	queryes = dict(parse_qsl(data.query))
	update_queryes = {key: value}
	queryes.pop(key) if value == None else queryes.update(update_queryes)
	return data._replace(query = urlencode(queryes))


def to_string(url):
	print(url.geturl())
	return url.geturl()

# Test Program
def test():

	u = url.make('https://hexlet.io/community?q=low')
	to_string(u) # https://hexlet.io/community?q=low
	
	u = url.set_scheme(u, 'http')
	url.to_string(u) # 'http://hexlet.io/community?q=low'
	
	u = url.set_path(u, '/404')
	url.to_string(u) # 'http://hexlet.io/404?q=low'
	
	url.get_query_param(u, 'q')
	'low'
	
	u = url.set_query_param(u, 'page', 5)
	url.to_string(u) # 'http://hexlet.io/404?q=low&page=5'

	u = url.set_query_param(u, 'q', 'high')
	url.to_string(u) # 'http://hexlet.io/404?q=high&page=5'

	u = url.set_query_param(u, 'q', None)
	url.to_string(u) # 'http://hexlet.io/404?page=5'

	
	"""
	data = urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
	print(data) # spam=1&eggs=2&bacon=0
	data = dict(parse_qsl(data))
	print(data) # {'spam': '1', 'eggs': '2', 'bacon': '0'}
	"""

if __name__ == '__main__':
	test()

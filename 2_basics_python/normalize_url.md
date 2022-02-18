ЗаданиеРеализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.
Функция принимает адреса в виде АДРЕС или http://АДРЕС, но всегда возвращает адрес в виде https://АДРЕС. На вход функции также может поступить адрес в уже нормализованном виде https://АДРЕС, в этом случае ничего менять не надо.

Решение учителя:

def normalize_url(url):
	https = 'https://'
	if url[:8] == https:
		return url
	else:
	if url[:7] == 'http://':
		return https + url[7:]
	else:
		return https + url

Моё решение:

def normalize_url(url):
	lenth = len('https://')
	https = 'https://'
	if url[:lenth] == https:
		return url
	else:
		lenth = len('http://')
	if url[:lenth] == 'http://':
		return https + url[lenth:]
	else:
		return https + url
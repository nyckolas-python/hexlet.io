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
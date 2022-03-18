def build_query_string(param):
	result = ''
	for i in param:
		result =''.join(str(i)+str(param[i])) + result
	return print(result)

# Test Program
param = {'per': 10, 'page': 1}
build_query_string(param)
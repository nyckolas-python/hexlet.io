from distutils import dep_util


def stringigy(input, replacer=' ', spaces_count=1):
	output = ''
	sep = replacer*spaces_count
	deepth = 1
	def inner(input, sep=sep, output=output, deepth=deepth):
		if type(input) in (str, int, float):
			return sep+str(input)
		if type(input) == dict:
			output = ''
			for k, v in input.items():
				if type(v) == dict:
					print(v)
					deepth += 1
					print(deepth)
					output += sep+str(k)+': '+inner(v)
					output = '{\n'+output+'}\n'					
					return output
				output += sep+str(k)+': '+str(v)+'\n'
			output = '{\n'+output+'}\n'
			deepth += 1
			return output # самый вложенный дикт
		return output
	return inner(input, sep, output, deepth)

data = { "hello": "world", "is": True, "nested": { "count": { "count": { "count": 5 } } } }

"""{
  hello: world
  is: True
  nested: {
   count: 5
  }
}
"""
#print(stringigy(data))
print(stringigy(data, replacer='|-', spaces_count=2))
data = 5
print(stringigy(data, replacer='|-', spaces_count=2))
data = 'nyckolas'
print(stringigy(data, replacer='|-', spaces_count=2))
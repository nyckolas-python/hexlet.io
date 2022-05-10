from distutils import dep_util
from webbrowser import get


def stringigy(input, replacer=' ', spaces_count=1):
	output = ''
	sep = replacer*spaces_count
	#deepth = 1
	def get_children(input):		
		return input.items()
	print(get_children(input))

	def inner(input, sep=sep, output=output, deepth=1):
		if type(input) in (str, int, float):
			return sep+str(input)
		if type(input) == dict:
			output = ''
			for k, v in input.items():
				if type(v) == dict:
					#sep += sep			
					output += sep+str(k)+': '+inner(v)
					output = '{\n'+output+'}\n'
					#print(v)
					#print(output)
					sep += sep			
					return output
				output += sep+str(k)+': '+str(v)+'\n'
			
			output = '{\n'+sep+output+'}\n'
			return output # самый вложенный дикт
		return output
	return inner(input, sep, output, 1)

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
#print(stringigy(data, replacer='|-', spaces_count=2))
data = 'nyckolas'
#print(stringigy(data, replacer='|-', spaces_count=2))
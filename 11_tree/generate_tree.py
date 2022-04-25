from pprint import pprint


def mkdir(name, children=[], meta={}):
	dir = {
		'name': name,
		'type': 'directory',
		'meta': meta,
		'children': children
	}
	return dir

def mkfile(name, meta={}):
	file = {
		'name': name,
		'type': 'file',
		'meta': meta
	}
	return file

def get_name(tree):
	return tree['name']

def get_meta(tree):
	return tree['meta']

def get_children(tree):
	return tree['children']

def is_directory(tree):
	return True if tree['type'] == 'directory' else False

def is_file(tree):
	return True if tree['type'] == 'file' else False

def test():
	
	tree = mkdir('etc', [
		mkfile('bashrc'),
		mkdir('consul', [
			mkfile('config.json'),
		]),
	])

	new_tree = mkdir('python-package', [
		mkfile('Makefile'),
		mkfile('Readme.md'),
		mkdir('dist'),
		mkdir('tests', [
			mkfile('test_solution.py'),
		]),
		mkfile('pyproject.toml'),
		mkdir('.venv', [
			mkdir('lib', [
				mkdir('lib', [
					mkdir('python3.6', [
						mkdir('site-pachages', [
							mkfile('hexlet-python-package.egg-link'),
						]),
					]),
				]),
			]),
		], {'owner': 'root', 'hidden': False}),
	], {'hidden': True})

	tree = mkdir('/', [mkfile('hexlet.log')], {'hidden': True})
	[file] = get_children(tree)
	print(is_file(file)) # True
	pprint(new_tree, sort_dicts=False)

'''
{'name': 'python-package',
'type': 'directory',
'meta': {'hidden': True},
'children': [{'name': 'Makefile', 'type': 'file', 'meta': {}},
			{'name': 'Readme.md', 'type': 'file', 'meta': {}},
			{'name': 'dist', 'type': 'directory', 'meta': {}, 'children': []},
			{'name': 'tests',
			'type': 'directory',
			'meta': {},
			'children': [{'name': 'test_solution.py',
							'type': 'file',
							'meta': {}}]},
			{'name': 'pyproject.toml', 'type': 'file', 'meta': {}},
			{'name': '.venv',
			'type': 'directory',
			'meta': {'owner': 'root', 'hidden': False},
			'children': [{'name': 'lib',
							'type': 'directory',
							'meta': {},
							'children': [{'name': 'lib',
										'type': 'directory',
										'meta': {},
										'children': [{'name': 'python3.6',
														'type': 'directory',
														'meta': {},
														'children': [{'name': 'site-pachages',
																	'type': 'directory',
																	'meta': {},
																	'children': [{'name': 'hexlet-python-package.egg-link',
																					'type': 'file',
																					'meta': {}}]}]}]}]}]}]}
'''
if __name__ == '__main__':
	test()

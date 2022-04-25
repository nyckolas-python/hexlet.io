from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file
from copy import deepcopy

def downcase_file_name(node):
	'''
	Ф-ция принимает на фход папку или файл.
	Приводит имена всех фалов во всех вложенных директориях к нижнему регистру.
	'''
	name = get_name(node)
	new_meta = deepcopy(get_meta(node))
	if is_file(node): # условие is_file True
		name = name.lower() # приводим имя в нижнем регистре
		return mkfile(name, new_meta) # возвращает новый файл с новым именем
	children = get_children(node) # 
	new_children = list(map(lambda child: downcase_file_name(child), children)) # рекурсивных обход
	new_tree = mkdir(name, new_children, new_meta)
	return new_tree

def test():
# Test Program

	tree = mkdir(
		'My Documents',
		[
			mkfile('AvAtAr.jpg', {'size': 100}),
			mkfile('phOtO.jpg', {'size': 150}),
			mkfile('tEst_nAmE.jpEg', {'size': 150}),
			mkdir('phOtO_DIR', [
				mkfile('AvAtAr_inside.jpg', {'size': 200})
			], {'hide': True})
		],
		{'hide': False}
	)

	file = mkfile('AvAtAr.jpg', {'size': 100})

	pprint(downcase_file_name(tree), sort_dicts=False)
	pprint(downcase_file_name(file), sort_dicts=False)
'''
{'name': 'My Documents',
 'type': 'directory',
 'meta': {'hide': False},
 'children': [{'name': 'avatar.jpg', 'type': 'file', 'meta': {'size': 100}},
              {'name': 'photo.jpg', 'type': 'file', 'meta': {'size': 150}},
              {'name': 'test_name.jpeg', 'type': 'file', 'meta': {'size': 150}},
              {'name': 'phOtO_DIR',
               'type': 'directory',
               'meta': {'hide': True},
               'children': [{'name': 'avatar_inside.jpg',
                             'type': 'file',
                             'meta': {'size': 200}}]}]}
{'name': 'avatar.jpg', 'type': 'file', 'meta': {'size': 100}}
'''

if __name__ == '__main__':
	test()
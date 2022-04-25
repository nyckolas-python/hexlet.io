from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file
from copy import deepcopy

def compress_images(tree):
	'''
	Ф-ция принимает на фход папку или файл, находит все файлы картинки (.jpg) и сжимает их в 2 раза.
	Возвращает обновленную директорию со сжатыми файлами и всеми остальными данными кторорые были нутри.
	'''
	def to_compress(node): # Ф-ция сжимает только файлы с расширением '.jpg'
		name = get_name(node)
		new_meta = deepcopy(get_meta(node))
		if name[-4:] == '.jpg' and is_file(node): # условие оконочание '.jpg' и is_file True
			new_meta['size'] = int(new_meta.get('size')/2) # изменяем параментр ['size'] в словаре 'meta'
			return mkfile(name, new_meta) # возвращает новый сжатый файл
		return node
	name = get_name(tree)
	new_meta = deepcopy(get_meta(tree))
	if is_directory(tree): # проверяем на входя файл или директория
		children = get_children(tree)[:] # если директория, клонируем всю вложенную структуру файлов и папок
		new_children = list(map(to_compress, children)) # сжимаем все файлы '.jpg'
		return mkdir(name, new_children, new_meta) 
	return to_compress(mkfile(name, new_meta))

def test():
# Test Program

	tree = mkdir(
		'my documents',
		[
			mkfile('avatar.jpg', {'size': 100}),
			mkfile('photo.jpg', {'size': 150}),
			mkfile('test_name.jpeg', {'size': 150}),
			mkdir('photo.jpg', [], {'hide': True})
		],
		{'hide': False}
	)

	file = mkfile('avatar.jpg', {'size': 100})

	pprint(compress_images(tree), sort_dicts=False)
	pprint(compress_images(file), sort_dicts=False)
'''
{'name': 'my documents',
 'type': 'directory',
 'meta': {'hide': False},
 'children': [{'name': 'avatar.jpg', 'type': 'file', 'meta': {'size': 50}},
              {'name': 'photo.jpg', 'type': 'file', 'meta': {'size': 75}},
              {'name': 'test_name.jpeg', 'type': 'file', 'meta': {'size': 150}},
              {'name': 'photo.jpg', 'type': 'file', 'meta': {'hide': True}}]}
{'name': 'avatar.jpg', 'type': 'file', 'meta': {'size': 50}}
'''

if __name__ == '__main__':
	test()
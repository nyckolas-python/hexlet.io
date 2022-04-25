from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file
from copy import deepcopy

def compress_images(node):
	'''
	Ф-ция принимает на фход папку или файл, находит все файлы картинки (.jpg) и сжимает их в 2 раза.
	Возвращает обновленную директорию со сжатыми файлами и всеми остальными данными кторорые были внутри.
	'''
	name = get_name(node)
	new_meta = deepcopy(get_meta(node))
	if is_file(node): # условие оконочание '.jpg' и is_file True
		if name[-4:] == '.jpg':
			new_meta['size'] = int(new_meta.get('size')/2) # изменяем параментр ['size'] в словаре 'meta'
		return mkfile(name, new_meta) # возвращает новый сжатый файл
	children = get_children(node) # если директория, клонируем всю вложенную структуру файлов и папок
	new_children = list(map(lambda child: compress_images(child), children)) # сжимаем все файлы '.jpg'
	new_tree = mkdir(name, new_children, new_meta)
	return new_tree

def test():
# Test Program

	tree = mkdir(
		'my documents',
		[
			mkfile('avatar.jpg', {'size': 100}),
			mkfile('photo.jpg', {'size': 150}),
			mkfile('test_name.jpeg', {'size': 150}),
			mkdir('photo.jpg', [
				mkfile('avatar_inside.jpg', {'size': 200})
			], {'hide': True})
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
              {'name': 'photo.jpg',
               'type': 'directory',
               'meta': {'hide': True},
<<<<<<< HEAD
               'children': [{'name': 'avatar_inside.jpg',
                             'type': 'file',
                             'meta': {'size': 100}}]}]}
=======
               'children': []}]}
>>>>>>> 609df2cb51494b4982897e5b74705b62764a0dfb
{'name': 'avatar.jpg', 'type': 'file', 'meta': {'size': 50}}
'''

if __name__ == '__main__':
	test()
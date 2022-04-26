from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file

def get_hidden_files_count(node):
	'''
	Ф-ция принимает каталог и подсчитывает количество скрытых файлов (начинаюся с точки ".")
	'''
	name = get_name(node)
	if is_file(node):
		if name[0] == '.':
			#print(name)
			return 1
		return 0
	children = get_children(node)
	count = list(map(get_hidden_files_count, children))	
	return sum(count)

# Test Program

tree = mkdir('/', [
		mkdir('.etc', [
			mkfile('.bashrc'),
			mkfile('.consul.cfg'),
		]),
		mkfile('hexletrc'),
		mkdir('bin', [
			mkfile('.ls'),
			mkfile('.cat'),
		]),
	])

print(get_hidden_files_count(tree)) # 4

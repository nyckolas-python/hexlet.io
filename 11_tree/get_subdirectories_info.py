from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file


def get_files_count(node):
	if is_file(node):
		return 1  
	children = get_children(node)
	descendant_counts = list(map(get_files_count, children))
	return sum(descendant_counts)

def get_subdirectories_info(node):
	children = get_children(node)
	# Нас интересуют только директории
	filtered = filter(is_directory, children)
	# Запускаем подсчёт для каждой директории
	result = map(
		lambda child: (get_name(child), get_files_count(child)),
		filtered,
	)
	return list(result)

tree = mkdir('/', [
	 mkdir('etc', [
		 mkdir('apache'),
		 mkdir('nginx', [
			 mkfile('nginx.conf'),
		 ]),
	 ]),
	 mkdir('consul', [
		 mkfile('config.json'),
		 mkfile('file.tmp'),
		 mkdir('data'),
	 ]),
	 mkfile('hosts'),
 	mkfile('resolve'),
 ])

print(get_subdirectories_info(tree))

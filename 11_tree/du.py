from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file


def get_size_of_file(node):
	if is_file(node):
		return get_meta(node)['size']
	children = get_children(node)
	size = list(map(get_size_of_file,children))
	return sum(size)

def du(node):
	children = get_children(node)
	# Запускаем подсчёт для каждой директории
	result = map(
		lambda child: (get_name(child), get_size_of_file(child)),
		children,
	)
	return sorted(list(result))

tree = mkdir('/', [
	mkdir('etc', [
		mkdir('apache'),
		mkdir('nginx', [
			mkfile('nginx.conf', {'size': 80}),
		]),
	]),
	mkdir('consul', [
		mkfile('config.json', {'size': 80}),
		mkfile('file.tmp', {'size': 80}),
		mkdir('data', [
			mkfile('file.tmp', {'size': 80}),
			mkfile('file.tmp', {'size': 80})
		]),
	]),
	mkfile('hosts', {'size': 80}),
	mkfile('resolve', {'size': 80}),
	])

print(du(tree))
# [('consul', 320), ('etc', 80), ('hosts', 80), ('resolve', 80)]
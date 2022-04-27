from generate_tree import *


def find_empty_dir_paths(tree):
	name = get_name(tree)
	children = get_children(tree)
	if len(children) == 0:
		return name
	dir_names = filter(lambda child: not is_file(child), children)
	empty_dir_names = list(map(
		lambda dir: find_empty_dir_paths(dir),
		dir_names
	))
	return flatten(empty_dir_names)

def find_empty_dir_with_deep(tree):
	# Внутренняя функция, которая может передавать аккумулятор
    # Аккумулятором выступает depth, переменная, содержащая текущую глубину
	def iter(node, depth):
		name = get_name(node)
		children = get_children(node)
		# Если детей нет, то добавляем директорию
		if len(children) == 0:
			return name
		# Если это второй уровень вложенности, и директория не пустая
        # то не имеет смысла смотреть дальше
		if depth == 1:
			# Почему возвращается именно пустой список?
            # Потому что снаружи выполняется flatten
            # Он раскрывает пустые списки
			return []
		# Оставляем только директории
		dir_paths = filter(is_directory, children)
		# Не забываем увеличивать глубину
		output = list(map(
            lambda child: iter(child, depth + 1),
            dir_paths,
          ))
		return flatten(output)
		#return output
	# Начинаем с глубины 0
	return iter(tree, 0)
		
# Test Program

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
		mkdir('data',[]),
	]),
	mkfile('hosts', {'size': 80}),
	mkdir('resolve',[]),
	])

print(find_empty_dir_paths(tree))

print(find_empty_dir_with_deep(tree))


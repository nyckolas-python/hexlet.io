from generate_tree import *
import os

def find_files_by_name(node, find:str) -> list:
	'''
	Ф-ция принимает на вход файловое дерево и подстроку.
	А возвращает список файлов имена которых содержат искомую подстроку.
	Ф-ция аккумулирует и возвращает полные пути файлов.
	'''
	# Внутренняя функция, которая передаёт аккумулятор
	# Аккумулятором выступает path, переменная, содержащая текущий путь
	def iter(node, path):
		name = get_name(node)
		#print(os.path.join(path, name)) # можно выводить на экран для нагляддности
		# 1. Проверяет тип узла. Если узел — это файл, тогда проверяем имя файла.
		if is_file(node):
			# 2. Если имя содержит искомую подстроку дописываем путь и возвращаем его.
			if find in name:
				path = os.path.join(path, name)
				return path
			# Если имя файла не содержит возвращаем пустой список.
			# flatten на выходе уберет пустые списки и сгладит список.
			return []
		# 3. В случае, если узел — директория, тогда получаем детей и для каждого ребёнка вновь
		# вызываем нашу функцию. Затем повторяем алгоритм заново.
		children = get_children(node)
		# 4. Вызов функции на каждом ребёнке возвращает свой собственный результат (путь к файлу).
		# Эти результаты образуют массив, которые нужно объединить с помощью тар().
		output = list(map(
			lambda child: iter(child, os.path.join(path, name)),
			children
		))
		# Перед возвратом "выпрямляем" список
		return flatten(output)
	# Вызываем вложенную ф-цию, в переменной path будет аккумулироваться путь.
	return iter(node, path = '')

# Test Program

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

print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/consul/config.json']
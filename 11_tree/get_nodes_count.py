from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file


def get_nodes_count(node):
	if is_file(node):
		return 1
	children = get_children(node)
	descendant_counts = list(map(get_nodes_count,children))
	return 1 + sum(descendant_counts)

tree = mkdir('/', [
		mkdir('etc', [
			mkfile('bashrc'),
			mkfile('consul.cfg'),
		]),
		mkfile('hexletrc'),
		mkdir('bin', [
			mkfile('ls'),
			mkfile('cat'),
		]),
	])

print(get_nodes_count(tree))

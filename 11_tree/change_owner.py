from pprint import pprint
from generate_tree import is_directory, is_file, mkdir, mkfile, get_name, get_children, get_meta, is_directory, is_file
from copy import deepcopy

def change_owner(node,owner):
	name = get_name(node)
	new_meta = deepcopy(get_meta(node))
	new_meta['owner'] = owner
	if is_file(node):
		return mkfile(name, new_meta)
	children = get_children(node)
	new_children = list(map(lambda child: change_owner(child,owner), children))
	new_tree = mkdir(name, new_children, new_meta)
	return new_tree

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

pprint(change_owner(tree, 'nyckolas'), sort_dicts=False)

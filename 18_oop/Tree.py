#!usr/bin/env python3

class Node:
    # Это класс узла.
    def __init__(self, data=u''):
        self.parent = None
        self.children = []
        self.data = data
        
    def add_node(self, data=u''):
        childNode = Node(data)
        childNode.parent = self
        self.children.append(childNode)
        return childNode
 
    def delete_from_tree(self, tree):
        for i in tree.nodes:
            if tree.nodes[i] == self:
                tree.nodes[i] = None
                break
        for child in self.children:
            child.delete_from_tree(tree)
        if self.parent != None:
            self.parent.children.remove(self)
            self.parent = None
        if tree.root == self:
            tree.root = None
 
 
class Tree:
    def __init__(self, rootData=u''):
        self.root = Node(rootData)
        self.nodes = {0: self.root}
        self.lastId = 0
 
    def add_node(self, index, data):
        childNode = self.nodes[index].add_node(data)
        self.lastId += 1
        self.nodes[self.lastId] = childNode
 
    def search(self, data, startNode=None):
        if startNode == None:
            startNode = self.root
        result = []
        if startNode.data == data:
            result.append(startNode)
            
        for i in startNode.children:
            result += self.search(data, i)
        return result

def test():
	tree = Tree()
	tree.add_node(0, '1')
	tree.add_node(1, '2')
	tree.add_node(1, '3')
	print('\n'.join(map(str, [list(tree.nodes.values())[x].data for x in tree.nodes])))

if __name__ == '__main__':
    test()

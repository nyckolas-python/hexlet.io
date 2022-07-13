from pprint import pprint

class TreeBuilder:
    def __init__(self) -> None:
        self.structure = []
        self.__name = 0
    
    def __enter__(self):
        print('hello')
        self.add_node()
        
    
    def __exit__(self, *args):
        print(f'exit - {args}')
    
    def add(self, name:str) -> list:
        self.__name = name
        self.add_leaf()
        
    def add_leaf(self):
        self.structure.append(self.__name)
    
    def add_node(self):
        self.structure.append(list(self.__name))

        
    def structure(self):
        pprint(self.structure)

def test():
    tree = TreeBuilder()
    with tree:
        tree.add('2nd')
        with tree:
            tree.add('3rd')
        tree.add('4th')

    tree.structure
    

if __name__ == '__main__':
    test()
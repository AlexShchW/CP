import sys

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.depths = {}

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self.depths[value] = 0
            print('DONE')
        else:
            if value in self.depths:
                print('ALREADY')
                return
            cur_depth = 0
            print('DONE')
            current_node = self.root
            while True:
                cur_depth += 1
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = Node(value)
                        self.depths[value] = cur_depth
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Node(value)
                        self.depths[value] = cur_depth
                        break
                    else:
                        current_node = current_node.right
    
    def search(self, value):
        if value in self.depths:
            print('YES')
        else:
            print('NO')
    
    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print('.' * self.depths[node.value] + str(node.value))
        self.print_tree(node.right)

tree = Tree()
while True:
    try:
        command, *value = input().split()
        if command == 'ADD':
            tree.add(int(value[0]))
        elif command == 'SEARCH':
            tree.search(int(value[0]))
        else:
            tree.print_tree(tree.root)
    except:
        break


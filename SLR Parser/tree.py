from anytree import Node
from anytree.exporter import UniqueDotExporter

class Tree_Node:
    def __init__(self, data):
        self.name = data
        self.children = []
    
    def add_child_node(self, child):
        self.children.append(child)


def create_tree(root):
    if root.children == []:
        return
    else:
        node = Node(root)
        for child in root.children:
            new_node = Node(child.name, parent = node)
            create_tree(child)
        exporter = UniqueDotExporter(root)
        exporter.to_dotfile("tree.dot")
        exporter.to_picture("tree.png")
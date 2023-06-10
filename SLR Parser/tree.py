class Tree_Node:
    def __init__(self, data):
        self.data = data
        self.child_nodes = []
    
    def add_child_node(self, child):
        self.child_nodes.append(child)
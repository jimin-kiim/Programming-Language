from anytree import Node
from anytree.exporter import UniqueDotExporter
import os

# node class needed to make parsing tree
class Tree_Node:
    def __init__(self, data):
        self.name = data # according to UniqueDotExporter library document
        self.children = [] # according to UniqueDotExporter library document
    
    def add_child_node(self, child):
        self.children.append(child)

# traversing the tree created by recurrence function 
def create_tree(root):
    if root.children == []: # termination condition (reached leaf nodes)
        return
    else: # not yet reached node
        root.children.reverse() 
        for child in root.children: 
            create_tree(child) # according to UniqueDotExporter library document
        exporter = UniqueDotExporter(root) # according to UniqueDotExporter library document
        exporter.to_picture("parse_tree.png") # according to UniqueDotExporter library document
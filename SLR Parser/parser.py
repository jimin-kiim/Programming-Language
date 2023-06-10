from parsing_table import parsing_table 
from grammar import grammar 
from tree import *
# from anytree.exporter import UniqueDotExporter
from treelib import Node, Tree

def parse(input):
    tokens = input.split(' ')
    state = 0
    stack = []
    symbol_index = 0
    stack.append(state)
    nodes = []
    while(1) :
        # print("state",state)
        if tokens[symbol_index] not in parsing_table[state]:
            print("reject")
            break
        cell_value = parsing_table[state][tokens[symbol_index]]
        # print("CELL VALUE", cell_value, "TOKEN", tokens[symbol_index])
        if cell_value == 'acc':
            print("accept")
            # tree = Tree()
            create_tree(nodes[0])
            # exporter = UniqueDotExporter(root)
            # exporter.to_picture("parsetree.png")
            break
        elif cell_value[0] == 's': # shift
            state = int(cell_value[1:])
            stack.append(state) # push the next state into the stack
            nodes.append(Tree_Node(tokens[symbol_index]))
            # print("STACK", stack)
            symbol_index += 1 # move the splitter to the right
        else: # reduce
            grammar_index = int(cell_value[1:])
            rhs = grammar[grammar_index][1]
            # print("RHS", rhs)
            size_of_rhs = len(rhs.split())
            parent = Tree_Node(grammar[grammar_index][0])
            for i in range(size_of_rhs): # Step 1. for A -> a, pop |a| contents from the stack 
                stack.pop()
                child = nodes.pop()
                parent.add_child_node(child)
            state = stack[-1]
            # print("STACK 1", stack)
            col_value = grammar[grammar_index][0] # Step 2. for A -> a, push GOTO(current state, A) into the stack
            state = parsing_table[state][col_value]
            stack.append(state)
            
            # for child_data in children_data:
                # parent.add_child_node(Node(child_data))
            nodes.append(parent)
            print(parent.name)
            # print("STACK 2", stack)
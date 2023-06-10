from parsing_table import parsing_table 
from grammar import grammar 
from tree import *
import time

def parse(input):
    tokens = input.split(' ') # get tokens from string
    state = 0 # start state
    stack = [] # stack to store state
    symbol_index = 0 # pointer to read input string 
    nodes = [] # list to store node

    stack.append(state) # stack initialization 
    
    while(1) :
        # REJECTED 
        if tokens[symbol_index] not in parsing_table[state]:
            print("Syntax Analyzing Result: reject") 
            if tokens[symbol_index] == '$': # error after reading all of tokens from the string
                print("Syntax Analyzing Error: ")
                print("  the code ended up with incomplete syntax.")
            else: # error during analyzing 
                print("Syntax Analyzing Error:")
                print(f"  error occured while reading '{tokens[symbol_index]}' in '{input}'", )
                print("  symbol pointer:", symbol_index)
                print("  state:",state)
                print("  stack:",stack)
            break
        
        # NOT REJECTED
        cell_value = parsing_table[state][tokens[symbol_index]]

        # ACCEPTED 
        if cell_value == 'acc':
            print("Syntax Analyzing Result: accept")
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("'parse_tree.png' is created.")
            create_tree(nodes[0])
            break

        # SHIFT
        elif cell_value[0] == 's':
            state = int(cell_value[1:]) # read the next state
            stack.append(state) # push the next state into the stack
            nodes.append(Tree_Node(tokens[symbol_index])) # save a new node
            symbol_index += 1 # move the splitter to the right

        # REDUCE
        else: 
            grammar_index = int(cell_value[1:]) # read the grammar index
            rhs = grammar[grammar_index][1] # read the string to be reduced
            size_of_rhs = len(rhs.split()) # the length of the tokens to be reduced
            parent = Tree_Node(grammar[grammar_index][0]) # save a new node 
            for i in range(size_of_rhs): # Step 1. for A -> a, pop |a| contents from the stack 
                stack.pop() # stack for saving state update

                # turn children nodes into parent node (reducing)
                child = nodes.pop() 
                parent.add_child_node(child)
            state = stack[-1] # apply updated state value
            col_value = grammar[grammar_index][0] # Step 2. for A -> a, push GOTO(current state, A) into the stack
            state = parsing_table[state][col_value] # read the table with new state
            stack.append(state) # update new state
            nodes.append(parent) # turn children nodes into parent node (reducing)
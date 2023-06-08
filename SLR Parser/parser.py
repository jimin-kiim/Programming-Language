from parsing_table import parsing_table 
from grammar import grammar 

input = "vtype id semi vtype id lparen rparen lbrace if lparen boolstr comp boolstr rparen lbrace rbrace"
tokens = input.split(' ')
tokens.append('$')
print(tokens)

state = 0
stack = []
symbol_index = 0
stack.append(state)
while(1) :
    print("state",state)
    cell_value = parsing_table[state][tokens[symbol_index]]
    if cell_value == 'acc':
        print("Accepted")
        break
    elif cell_value[0] == 's': # shift
        state = int(cell_value[1:])
        stack.append(state) # push the next state into the stack
        symbol_index += 1 # move the splitter to the right
    else: # reduce
        grammar_index = int(cell_value[1:])
        rhs = grammar[grammar_index][1]
        size_of_rhs = len(rhs.split())
        for i in range(size_of_rhs - 1): # Step 1. for A -> a, pop |a| contents from the stack 
            stack.pop()
        col_value = grammar[grammar_index][0] # Step 2. for A -> a, push GOTO(current state, A) into the stack
        state = parsing_table[state][col_value]
        stack.append(state)
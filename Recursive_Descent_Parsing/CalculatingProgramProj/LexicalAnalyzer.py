from constants import *
# from global_variables import *
import global_variables as g

def get_char():
    # global index
    # global input
    # global next_char
    # global char_class
    # print(">>>>INPUT",g.input)
    # print(">>>>INDEX",g.index)
    g.next_char = g.input[g.index]
    g.index += 1
    if  g.next_char != "\0" :
        if g.next_char.isalpha():
            g.char_class = LETTER
        elif g.next_char.isdigit():
            g.char_class = DIGIT
        else:
            g.char_class = UNKNOWN
    else:
        g.char_class = EOF

def get_non_blank():
    # global next_char
    while g.next_char.isspace():
        get_char()

def add_char():
    # global g.next_char
    # global lexeme
    
    g.lexeme.append(g.next_char)

def lookup(character):
    # global next_token 
    if character == "(":
        add_char()
        g.next_token = LEFT_PAREN
    elif character == ")":
        add_char()
        g.next_token = RIGHT_PAREN
    elif character == "+":
        add_char()
        g.next_token = ADD_OP
    elif character == "-":
        add_char()
        g.next_token = SUB_OP
    elif character == "*":
        add_char()
        g.next_token = MULT_OP
    elif character == "/":
        add_char()
        g.next_token = DIV_OP
    elif character == "=":
        add_char()
        g.next_token = ASSIGN_OP
    elif character == ";":
        add_char()
        g.next_token = SEMI_COLON
    else:
        add_char()
        g.next_token = "\0"
    return g.next_token

def lexical():
    # global char_class
    # global next_token
    # global next_char
    # global lexeme

    g.lexeme = []
    get_non_blank()
    if g.char_class == LETTER:
        add_char()
        get_char()
        while g.char_class == LETTER or g.char_class == DIGIT:
            add_char()
            get_char()
        g.next_token = IDENT
    elif g.char_class == DIGIT:
        add_char()
        get_char()
        while g.char_class == DIGIT:
            add_char()
            get_char()
        g.next_token = CONST
    elif g.char_class == UNKNOWN:
        lookup(g.next_char)
        get_char()
    elif g.char_class == EOF:
        g.next_token = EOF
        g.lexeme = "EOF"
    print_lexeme = ''.join(g.lexeme)
    print("Next token is", g.next_token, "Next lexeme is", print_lexeme )
    return g.next_token
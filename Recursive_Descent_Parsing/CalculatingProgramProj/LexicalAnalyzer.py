from constants import *
from global_variables import *

def get_char():
    global index
    global input
    global next_char
    global char_class

    next_char = input[index]
    index += 1
    if  next_char != "\0" :
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        char_class = EOF

def get_non_blank():
    global next_char
    while next_char.isspace():
        get_char()

def add_char():
    global next_char
    global lexeme
    
    lexeme.append(next_char)

def lookup(character):
    global next_token 
    if character == "(":
        add_char()
        next_token = LEFT_PAREN
    elif character == ")":
        add_char()
        next_token = RIGHT_PAREN
    elif character == "+":
        add_char()
        next_token = ADD_OP
    elif character == "-":
        add_char()
        next_token = SUB_OP
    elif character == "*":
        add_char()
        next_token = MULT_OP
    elif character == "/":
        add_char()
        next_token = DIV_OP
    elif character == "=":
        add_char()
        next_token = ASSIGN_OP
    elif character == ";":
        add_char()
        next_token = SEMI_COLON
    else:
        add_char()
        next_token = "\0"
    return next_token

def lexical():
    global char_class
    global next_token
    global next_char
    global lexeme

    lexeme = []
    get_non_blank()
    if char_class == LETTER:
        add_char()
        get_char()
        while char_class == LETTER or char_class == DIGIT:
            add_char()
            get_char()
        next_token = IDENT
    elif char_class == DIGIT:
        add_char()
        get_char()
        while char_class == DIGIT:
            add_char()
            get_char()
        next_token = CONST
    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char()
    elif char_class == EOF:
        next_token = EOF
        lexeme = "EOF"
    print_lexeme = ''.join(lexeme)
    print("Next token is", next_token, "Next lexeme is", print_lexeme )
    return next_token
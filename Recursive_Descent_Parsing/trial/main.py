import sys

input = ""
next_token = ""
index = 0
next_char = 0
char_class = 0
lex_len = 0
lexeme = []

EOF = 100

LETTER = 0
DIGIT = 1
UNKNOWN = 99

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

def read_file():
    string = ""
    input_file = sys.argv[1]
    with open(input_file,'r') as filereader:
        for row in filereader:
            string += row
    return string 

def get_char():
    global index
    global input
    global next_char
    global char_class

    next_char = input[index]
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
    global lex_len
    global next_char
    if lex_len <= 98:
        # print("lex_len")
        lexeme[lex_len] = next_char
        lex_len += 1
        lexeme[lex_len] = 0
    else:
        print("Error- lexeme is too long")

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
    else:
        add_char()
        next_token = "\0"
    return next_token

def lex():
    global char_class
    global next_token
    global lex_len
    global lexeme
    lex_len = 0
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
        next_token = INT_LIT
    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char()
    elif char_class == EOF:
        next_token = "\0"
        lexeme[0] = "\0"
    print("Next token is", next_token, "Next lexeme is", lexeme )
    return next_token


def main():
    global input 
    input = read_file()
    get_char()
    lex()
    while(next_token):
        lex()


if __name__ == "__main__":
    main()
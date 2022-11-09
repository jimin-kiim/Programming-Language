from constants import *
from global_variables import *
from LexicalAnalyzer import *

def factortail():
    print("Enter <factortail>")
    if next_token == MULT_OP:
        lexical()
        factor()
        factortail()
    elif next_token == "EOF":
        lexical()
    else:
        print("Error")
    print("Exit <factortail>")

def factor():
    print("Enter <factor>")
    if next_token == IDENT or next_token == CONST:
        lexical()
    elif next_token == LEFT_PAREN:
        lexical()
        expression()
        if next_token == RIGHT_PAREN:
            lexical()
        else:
            print("Error")
    else:
        print("Error")
    print("Exit <factor>")

def termtail():
    print("Enter <termtail>")
    if next_token == ADD_OP:
        lexical()
        term()
        termtail()
    elif next_token == "EOF":
        lexical()
    else:
        print("Error")
    print("Exit <termtail>")

def term():
    print("Enter <term>")
    factor()
    factortail()
    print("Exit <term>")

def expression():
    global next_token
    print("Enter <expression>")
    term()
    termtail()
    print("Exit <expression>")

def statement():
    global next_token
    print("Enter <statement>")
    if next_token == IDENT:
        lexical()
        if next_token == ASSIGN_OP:
            lexical()
            expression()
        else:
            print("Error")
    else:
        print("Error")
    print("Exit <statement>")

def statements():
    global next_token
    print("Enter <statements>")
    statement()
    while next_token == SEMI_COLON:
        lexical()
        statement()
    print("Exit <statements>")

def program():
    global next_token
    print("Enter <program>")
    statements()
    print("Exit <program>")

from constants import *
import global_variables as g
from LexicalAnalyzer import *

def factortail():
    print("Enter <factortail>")
    while g.next_token == MULT_OP:
        lexical()
        factor()
    print("Exit <factortail>")

def factor():
    print("Enter <factor>")
    if g.next_token == IDENT or g.next_token == CONST:
        lexical()
    elif g.next_token == LEFT_PAREN:
        lexical()
        expression()
        
        if g.next_token == RIGHT_PAREN:
            lexical()
        else:
            print(">>>>>",g.next_token,g.next_char)
            print("Error")
    else:
        print(">>>>>",g.next_token,g.next_char)
        print("Error")
    print("Exit <factor>")

def termtail():
    print("Enter <termtail>")
    while g.next_token == ADD_OP:
        lexical()
        term()
    print("Exit <termtail>")

def term():
    print("Enter <term>")
    factor()
    factortail()
    print("Exit <term>")

def expression():
    print("Enter <expression>")
    term()
    termtail()
    print("Exit <expression>")

def statement():
    print("Enter <statement>")
    if g.next_token == IDENT:
        lexical()
        if g.next_token == ASSIGN_OP:
            lexical()
            expression()
        else:
            print("Error")
    else:
        print("Error")
    print(f"ID: {g.ident_num}; CONST: {g.const_num}; OP: {g.op_num};")
    g.ident_num = 0
    g.const_num = 0
    g.op_num = 0
    print("Exit <statement>")

def statements():
    print("Enter <statements>")
    statement()
    while g.next_token == SEMI_COLON:
        lexical()
        statement()
    print("Exit <statements>")

def program():
    print("Enter <program>")
    statements()
    print("Exit <program>")

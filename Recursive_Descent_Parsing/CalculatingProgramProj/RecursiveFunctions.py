from constants import *
# from global_variables import *
import global_variables as g
from LexicalAnalyzer import *

def factortail():
    print("Enter <factortail>")
    print(">>>>",g.next_token)
    if g.next_token == MULT_OP:
        lexical()
        factor()
        factortail()
    elif g.next_token == EOF:
        lexical()
    else:
        print("Error")
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
            print("Error")
    else:
        print("Error")
    print("Exit <factor>")

def termtail():
    print("Enter <termtail>")
    if g.next_token == ADD_OP:
        lexical()
        term()
        termtail()
    elif g.next_token == "\0":
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

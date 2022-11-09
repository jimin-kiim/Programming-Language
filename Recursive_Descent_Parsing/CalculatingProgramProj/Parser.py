from constants import *
from global_variables import *
from LexicalAnalyzer import *

def factor():
    print("Enter <factor>")
    if next_token == IDENT or next_token == INT_LIT:
        lex()
    else:
        if next_token == LEFT_PAREN:
            lex()
            expression()
            if next_token == RIGHT_PAREN:
                lex()
            else:
                print("Error")
        else:
            print("Error")
    print("Exit <factor>")

def term():
    print("Enter <term>")
    factor()
    while next_token == MULT_OP or next_token == DIV_OP:
        lex()
        factor()
    print("Exit <term>")

def expression():
    global next_token
    print("Enter <expression>")
    term()
    while next_token == ADD_OP or next_token == SUB_OP:
        lex()
        term()
    print("Exit <expression>")
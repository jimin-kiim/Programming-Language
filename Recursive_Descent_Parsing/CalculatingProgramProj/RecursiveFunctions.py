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
    if g.next_token == IDENT:
        lexeme_as_string = ''.join(g.lexeme)
        # print(">>>>>>>",lexeme_as_string,g.identifier_names)
        if lexeme_as_string not in g.identifier_names:
            g.error = f"(Error) “정의되지 않은 변수({lexeme_as_string})가 참조됨”"
        lexical()
    elif g.next_token == CONST:
        lexical()
    elif g.next_token == LEFT_PAREN:
        lexical()
        expression()
        
        if g.next_token == RIGHT_PAREN:
            lexical()
        else:
            # print(">>>>>ELIF",g.next_token,g.next_char)
            print("Error")
    elif g.next_token == ADD_OP or g.next_token == MULT_OP:
        lexeme_as_string = ''.join(g.lexeme)
        g.warning = f"(Warning) “중복 연산자({lexeme_as_string}) 제거”"
    else:
        # print(">>>>>ELSE",g.next_token,g.next_char)
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
        lexeme_as_string = ''.join(g.lexeme)
        ident = Ident(lexeme_as_string)
        g.identifier_names.append(ident.name)
        lexical()
        if g.next_token == ASSIGN_OP:
            lexical()
            expression()
        else:
            print("Error")
    else:
        print("Error")
    
    print(f"ID: {g.ident_num}; CONST: {g.const_num}; OP: {g.op_num};")

    if g.warning:
        print(g.warning)
    if g.error:
        print(g.error)
    if g.warning is None and g.error is None:
        print("(OK)")

    g.ident_num = 0
    g.const_num = 0
    g.op_num = 0
    g.warning = None
    g.error = None

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

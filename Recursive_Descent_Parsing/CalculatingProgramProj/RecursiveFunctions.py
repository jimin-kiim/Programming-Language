from constants import *
import global_variables as g
from LexicalAnalyzer import *
from calculating import *

def update_refined_expression():
    lexeme_as_string = ''.join(g.lexeme)
    g.refined_expression.append(lexeme_as_string)

def factortail():
    while g.next_token == MULT_OP:
        update_refined_expression()
        lexical()
        factor()

def factor():
    if g.next_token == IDENT:
        lexeme_as_string = ''.join(g.lexeme)
        valid_ident_names = [ ident.name for ident in g.identifiers if ident.is_defined ]
        all_ident_names = [ ident.name for ident in g.identifiers]
        if lexeme_as_string not in valid_ident_names:
            g.error = f"(Error) “정의되지 않은 변수({lexeme_as_string})가 참조됨”"
            g.should_be_calculated = False
            if lexeme_as_string not in all_ident_names:
                ident = Ident(lexeme_as_string)
                g.identifiers.add(ident)
        else:
            ident = [ ident for ident in g.identifiers if ident.name == lexeme_as_string ]
            g.refined_expression.append(ident[0]) 
        lexical()
    elif g.next_token == CONST:
        update_refined_expression()
        lexical()
    elif g.next_token == LEFT_PAREN:
        update_refined_expression()
        lexical()
        expression()
        
        if g.next_token == RIGHT_PAREN:
            update_refined_expression()
            lexical()
        else:
            print("Error")
    elif g.next_token == ADD_OP or g.next_token == MULT_OP:
        lexeme_as_string = ''.join(g.lexeme)
        g.refined_expression.pop()
        g.warning = f"(Warning) “중복 연산자({lexeme_as_string}) 제거”"
    else:
        print("Error")

def termtail():
    while g.next_token == ADD_OP:
        update_refined_expression()
        lexical()
        term()

def term():
    factor()
    factortail()

def expression():
    term()
    termtail()

def statement():
    if g.next_token == IDENT:
        lexeme_as_string = ''.join(g.lexeme)
        g.ident = Ident(lexeme_as_string)
        lexical()
        if g.next_token == ASSIGN_OP:
            lexical()
            expression()
        else:
            print("Error")
    else:
        print("Error")
    
    print(f"ID: {g.ident_num}; CONST: {g.const_num}; OP: {g.op_num};")
    if g.should_be_calculated: # 정의되지 않은 변수가 없어서 계산이 가능할 때 
        g.ident.value = evaluate(g.refined_expression) # 우변 계산하고 대입
        g.ident.is_defined = True # 정의된 변수임을 저장. 
    
    g.identifiers.add(g.ident) # 정의된 변수든 아니든 모든 ident 모아두기. 
    
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
    g.refined_expression = []
    g.should_be_calculated = True

def statements():
    statement()
    while g.next_token == SEMI_COLON:
        lexical()
        statement()
    print("Result ==>",end="")
    for ident in g.identifiers:
        print(f" {ident.name}: {ident.value};", end="")

    print("")

def program():
    statements()

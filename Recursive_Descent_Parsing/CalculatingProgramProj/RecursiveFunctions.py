from constants import *
import global_variables as g
from LexicalAnalyzer import *
from calculating import *
class ParsingProgram:
    def __init__(self):
        # self.ident_num = 0
        # self.const_num = 0
        # self.op_num = 0

        self.ident = None
        self.identifiers = set()

        self.refined_expression = []
        self.warning = None
        self.error = None
        self.should_be_calculated = True
        self.statement_to_be_printed = []

    def update_refined_expression(self):
        lexeme_as_string = ''.join(g.lexeme)
        self.refined_expression.append(lexeme_as_string)
        self.statement_to_be_printed.append(" "+lexeme_as_string)

    def factortail(self):
        while g.next_token == MULT_OP:
            self.update_refined_expression()
            lexical()
            self.factor()

    def factor(self):
        if g.next_token == IDENT:
            lexeme_as_string = ''.join(g.lexeme)
            valid_ident_names = [ ident.name for ident in self.identifiers if ident.is_defined ]
            all_ident_names = [ ident.name for ident in self.identifiers]
            if lexeme_as_string not in valid_ident_names:
                self.error = f"(Error) “정의되지 않은 변수({lexeme_as_string})가 참조됨”"
                self.should_be_calculated = False
                if lexeme_as_string not in all_ident_names:
                    ident = Ident(lexeme_as_string)
                    self.identifiers.add(ident)
            else:
                ident = [ ident for ident in self.identifiers if ident.name == lexeme_as_string ]
                self.refined_expression.append(ident[0]) 
            self.statement_to_be_printed.append(" "+lexeme_as_string)
            lexical()
        elif g.next_token == CONST:
            self.update_refined_expression()
            lexical()
        elif g.next_token == LEFT_PAREN:
            self.update_refined_expression()
            lexical()
            self.expression()
            
            if g.next_token == RIGHT_PAREN:
                self.update_refined_expression()
                lexical()
            else:
                print("Error")
        elif g.next_token == ADD_OP or g.next_token == MULT_OP:
            lexeme_as_string = ''.join(g.lexeme)
            self.refined_expression.pop()
            self.statement_to_be_printed.pop()
            self.warning = f"(Warning) “중복 연산자({lexeme_as_string}) 제거”"
        else:
            print("Error")

    def termtail(self):
        while g.next_token == ADD_OP:
            self.update_refined_expression()
            lexical()
            self.term()

    def term(self):
        self.factor()
        self.factortail()

    def expression(self):
        self.term()
        self.termtail()

    def statement(self):
        if g.next_token == IDENT:
            lexeme_as_string = ''.join(g.lexeme)
            self.ident = Ident(lexeme_as_string)
            self.statement_to_be_printed.append(lexeme_as_string)
            lexical()
            if g.next_token == ASSIGN_OP:
                lexeme_as_string = ''.join(g.lexeme)
                self.statement_to_be_printed.append(" "+lexeme_as_string)
                lexical()
                self.expression()
            else:
                print("Error")
        else:
            print("Error")

        self.statement_to_be_printed.append(";")
        lexeme_as_string = ''.join(g.lexeme)
        print(''.join(self.statement_to_be_printed))
        print(f"ID: {g.ident_num}; CONST: {g.const_num}; OP: {g.op_num};")
        if self.should_be_calculated: # 정의되지 않은 변수가 없어서 계산이 가능할 때 
            self.ident.value = evaluate(self.refined_expression) # 우변 계산하고 대입
            self.ident.is_defined = True # 정의된 변수임을 저장. 
        
        self.identifiers.add(self.ident) # 정의된 변수든 아니든 모든 ident 모아두기. 
        
        if self.warning:
            print(self.warning)
        if self.error:
            print(self.error)
        if self.warning is None and self.error is None:
            print("(OK)")

        self.ident_num = 0
        self.const_num = 0
        self.op_num = 0
        self.warning = None
        self.error = None
        self.refined_expression = []
        self.should_be_calculated = True
        self.statement_to_be_printed = []

    def statements(self):
        self.statement()
        while g.next_token == SEMI_COLON:
            lexical()
            self.statement()
        print("Result ==>",end="")
        for ident in self.identifiers:
            print(f" {ident.name}: {ident.value};", end="")
        print("")

    def program(self):
        self.statements()

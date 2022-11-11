from constants import *
import global_variables as g
from LexicalAnalyzer import *
from Calculator import *

class ParsingProgram:
    def __init__(self):
        self.ident = None
        self.identifiers = []

        self.warning = None
        self.error = None
        self.should_be_calculated = True
        self.refined_expression = []
        self.statement_to_be_printed = []

        self.lexical_analyzer = LexicalAnalyzer()
        self.calculator = Calculator()

    def update_refined_expression(self):
        self.refined_expression.append(g.token_string)
        self.statement_to_be_printed.append(" " + g.token_string)

    def factortail(self):
        while g.next_token == MULT_OP:
            self.update_refined_expression()
            self.lexical_analyzer.lexical()
            self.factor()

    def factor(self):
        if g.next_token == IDENT:
            valid_ident_names = [ ident.name for ident in self.identifiers if ident.is_defined ]
            all_ident_names = [ ident.name for ident in self.identifiers]
            if g.token_string not in valid_ident_names:
                self.error = f"(Error) “정의되지 않은 변수({g.token_string})가 참조됨”"
                self.should_be_calculated = False
                if g.token_string not in all_ident_names:
                    ident = Ident(g.token_string)
                    self.identifiers.append(ident)
            else:
                ident = [ ident for ident in self.identifiers if ident.name == g.token_string ]
                self.refined_expression.append(ident[0]) 
            self.statement_to_be_printed.append(" " + g.token_string)
            self.lexical_analyzer.lexical()
        
        elif g.next_token == CONST:
            self.update_refined_expression()
            self.lexical_analyzer.lexical()
        
        elif g.next_token == LEFT_PAREN:
            self.update_refined_expression()
            self.lexical_analyzer.lexical()
            self.expression()
            
            if g.next_token == RIGHT_PAREN:
                self.update_refined_expression()
                self.lexical_analyzer.lexical()
            else:
                print("Error")
        
        elif g.next_token == ADD_OP or g.next_token == MULT_OP:
            self.refined_expression.pop()
            self.statement_to_be_printed.pop()
            self.warning = f"(Warning) “중복 연산자({g.token_string}) 제거”"
        
        else:
            print("Error")

    def termtail(self):
        while g.next_token == ADD_OP:
            self.update_refined_expression()
            self.lexical_analyzer.lexical()
            self.term()

    def term(self):
        self.factor()
        self.factortail()

    def expression(self):
        self.term()
        self.termtail()

    def statement(self):
        if g.next_token == IDENT:
            self.ident = Ident(g.token_string)
            self.statement_to_be_printed.append(g.token_string)
            self.lexical_analyzer.lexical()

            if g.next_token == ASSIGN_OP:
                self.statement_to_be_printed.append(" " + g.token_string)
                self.lexical_analyzer.lexical()
                self.expression()
            else:
                print("Error")
        
        else:
            print("Error")

        self.statement_to_be_printed.append(";")
        print(''.join(self.statement_to_be_printed))
        print(f"ID: {g.ident_num}; CONST: {g.const_num}; OP: {g.op_num};")

        if self.should_be_calculated: # 정의되지 않은 변수가 없어서 계산이 가능할 때 
            self.ident.value = self.calculator.evaluate(self.refined_expression) # 우변 계산하고 대입
            self.ident.is_defined = True # 정의된 변수임을 저장. 
        
        self.identifiers.append(self.ident) # 정의된 변수든 아니든 모든 ident 모아두기. 
        
        if self.warning:
            print(self.warning)
        if self.error:
            print(self.error)
        if self.warning is None and self.error is None:
            print("(OK)")
        print("")

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
            self.lexical_analyzer.lexical()
            self.statement()
        
        print("Result ==>",end="")
        for ident in self.identifiers:
            print(f" {ident.name}: {ident.value};", end="")
        print("")

    def program(self):
        self.statements()

from constants import *
import global_variables as g
from LexicalAnalyzer import *

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

    def statement(self):
        print("Enter <statement>")
        if g.next_token == CALL:
            self.lexical_analyzer.lexical()

            if g.next_token == IDENT:
                self.lexical_analyzer.lexical()
                if g.next_token == SEMI_COLON:
                    self.lexical_analyzer.lexical()
                else:
                    print("Error")
            else:
                print("Error")
        elif g.next_token == PRINT_ARI or  g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
            else:
                print("Error")
        else:
            print("Error")
        print("Exit <statement>")

    def statements(self):
        print("Enter <statements>")
        while g.next_token == CALL or  g.next_token == PRINT_ARI or g.next_token == IDENT:
            self.statement()
        print("Exit <statements>")
        
    def var_list(self):
        print("Enter <var_list>")
        if g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            while g.next_token == COMMA:
                self.lexical_analyzer.lexical()
                if g.next_token == IDENT:
                    self.lexical_analyzer.lexical()
                else:
                    print("Error")
        else:
            print("Error")
        print("Exit <var_list>")

    def var_definition(self):
        print("Enter <var_definition>")
        if g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_list()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
            else:
                print("Error")
        else:
            print("Error")
        print("Exit <var_definition>")

    def var_definitions(self):
        print("Enter <var_definitions>")
        self.var_definition()
        while g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_definition()
        print("Exit <var_definitions>")

    def function_body(self):
        print("Enter <function_body>")
        if g.next_token == VARIABLE:
            self.var_definitions()
            self.lexical_analyzer.lexical()
            self.statements()
        elif g.next_token == CALL or g.next_token == PRINT_ARI or g.next_token == IDENT:
            # self.lexical_analyzer.lexical()
            self.statements()
        else:
            print("Error")
        print("Exit <function_body>")

    def function(self):
        print("Enter <function>")
        if g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            if g.next_token == LEFT_BRACE:
                self.lexical_analyzer.lexical()
                self.function_body()
                if g.next_token == RIGHT_BRACE:
                    self.lexical_analyzer.lexical()
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
        print("Exit <function>")

    def functions(self):
        print("Enter <functions>")
        self.function()

        while g.next_token != EOF:
            self.lexical_analyzer.lexical()
            self.function()
        print("Exit <functions>")

    def start(self):
        print("Enter <start>")
        self.functions()
        print("Exit <start>")

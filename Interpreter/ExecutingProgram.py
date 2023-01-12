from constants import *
import global_variables as g
from LexicalAnalyzer import *
from ActivationRecord import *

class ExecutingProgram:
    def __init__(self):
        self.local_variables = []
        self.line_number = 0 
        self.current_ari = None
        # self.aris = []
        # self.run_time_stack = []
        self.lexical_analyzer = LexicalAnalyzer()

    def statement(self):
        # print("Enter <statement>")
        if g.next_token == CALL:
            self.lexical_analyzer.lexical()

            if g.next_token == IDENT :
                if g.token_string not in g.function_names:
                    print("\"Call to undefined function:",g.token_string+"\"")
                    exit()
                self.current_ari.callees.append(g.token_string)
                self.lexical_analyzer.lexical()
                if g.next_token == SEMI_COLON:
                    self.line_number += 1
                    self.lexical_analyzer.lexical()
        elif g.next_token == PRINT_ARI or  g.next_token == IDENT:
            self.lexical_analyzer.lexical()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
        self.line_number = 0 
        # print("Exit <statement>")

    def statements(self):
        # print("Enter <statements>")
        while g.next_token == CALL or  g.next_token == PRINT_ARI or g.next_token == IDENT:
            self.statement()
        # print("Exit <statements>")
        
    def var_list(self):
        # print("Enter <var_list>")
        # print("!!!!!!",g.token_string)
        # if g.token_string in self.local_variables:
            # print("\"Duplicate declaration of the identifier:",g.token_string+"\"")
        # else:
            # self.local_variables.append(g.token_string)
        
        if g.next_token == IDENT:
            self.current_ari.local_variables.append(g.token_string)
            self.lexical_analyzer.lexical()
            while g.next_token == COMMA:
                self.lexical_analyzer.lexical()
                
                # self.local_variables.append(g.token_string)
                self.current_ari.local_variables.append(g.token_string)
                if g.next_token == IDENT:
                    self.lexical_analyzer.lexical()
        # print("Exit <var_list>")

    def var_definition(self):
        # print("Enter <var_definition>")
        if g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_list()
            if g.next_token == SEMI_COLON:
                self.lexical_analyzer.lexical()
        # print("Exit <var_definition>")

    def var_definitions(self):
        # print("Enter <var_definitions>")
        self.var_definition()
        while g.next_token == VARIABLE:
            self.lexical_analyzer.lexical()
            self.var_definition()
        # print("Exit <var_definitions>")

    def function_body(self):
        # print("Enter <function_body>")
        # self.local_variables = []
        if g.next_token == VARIABLE:
            self.var_definitions()
            self.statements()
        elif g.next_token == CALL or g.next_token == IDENT:
            self.statements()
        elif g.next_token == PRINT_ARI :
            self.current_ari.set_is_there_print_ari_true()
        # print("LOCAL_VARIABLES", self.local_variables)
        # print("Exit <function_body>")

    def function(self):
        # print("Enter <function>")
        if g.next_token == IDENT:
            # self.function_names.append(g.token_string)
            self.current_ari = ActivationRecord(g.token_string)
            function_name = g.token_string
            
            self.lexical_analyzer.lexical()
            if g.next_token == LEFT_BRACE:
                self.lexical_analyzer.lexical()
                self.function_body()
                if g.next_token == RIGHT_BRACE:
                    self.lexical_analyzer.lexical()
            
        g.aris.append(self.current_ari)
        # print(g.aris)
        if function_name == "main":
            g.run_time_stack.append(self.current_ari)
            self.current_ari.set_is_called_true()
        # print(g.run_time_stack)
        # for ari in g.run_time_stack:
            # print("!!!!",ari.name)
        # print("Exit <function>")

    def functions(self):
        # print("Enter <functions>")
        self.function()

        while g.next_token == IDENT:
            self.function()
        # print("Exit <functions>")

    def start(self):
        # print("Enter <start>")
        self.functions()
        # print(self.function_names)
        # print("Exit <start>")
from constants import *
import global_variables as g
from Ident import *

class LexicalAnalyzer:
    char_class = 0
    next_char = 0
    index = 0

    # character를 한 자를 읽어 charater의 Type을 알아냅니다. 
    def get_char(self):
        LexicalAnalyzer.next_char = g.input[LexicalAnalyzer.index]
        LexicalAnalyzer.index += 1 # 다음 번에 함수 실행 시 현재 character의 다음 character를 읽을 수 있도록. 
        if  LexicalAnalyzer.next_char != "\0" :
            if LexicalAnalyzer.next_char.isalpha():
                LexicalAnalyzer.char_class = LETTER
            elif LexicalAnalyzer.next_char.isdigit():
                LexicalAnalyzer.char_class = DIGIT
            else:
                LexicalAnalyzer.char_class = UNKNOWN
        else:
            LexicalAnalyzer.char_class = EOF

    # UNKNOWN으로 판별난 character가 빈칸은 아니였는지 다시 체크 후 빈칸이었다면 다시 체크
    def get_non_blank(self):
        while LexicalAnalyzer.next_char.isspace():
            self.get_char()

    def add_char(self):
        g.lexeme.append(LexicalAnalyzer.next_char)

    def lookup(self,character):
        if character == "(":
            self.add_char()
            g.next_token = LEFT_PAREN

        elif character == ")":
            self.add_char()
            g.next_token = RIGHT_PAREN

        elif character == "+":
            self.add_char()
            g.next_token = ADD_OP
            g.op_num += 1

        elif character == "-":
            self.add_char()
            g.next_token = SUB_OP
            g.op_num += 1

        elif character == "*":
            self.add_char()
            g.next_token = MULT_OP
            g.op_num += 1

        elif character == "/":
            self.add_char()
            g.next_token = DIV_OP
            g.op_num += 1

        elif character == ":":
            self.add_char()
            g.next_token = ASSIGN_OP

        elif character == "=":
            self.add_char()
            g.next_token = ASSIGN_OP

        elif character == ";":
            self.add_char()
            g.next_token = SEMI_COLON
            
        else:
            self.add_char()
            g.next_token = "\0"

    def lexical(self):
        g.lexeme = []
        self.get_non_blank()

        if LexicalAnalyzer.char_class == LETTER: # lexeme이 LETTER로 시작한다면 
            self.add_char()
            self.get_char()
            while LexicalAnalyzer.char_class == LETTER or LexicalAnalyzer.char_class == DIGIT: # LETTER나 DIGIT로 이루어진 부분까지 
                self.add_char()
                self.get_char()
            g.next_token = IDENT # 하나의 lexeme으로 인식 후 이의 타입이 Identifier 임을 저장. 
            g.ident_num += 1
        
        elif LexicalAnalyzer.char_class == DIGIT: # 숫자로 시작한다면 
            self.add_char()
            self.get_char()
            while LexicalAnalyzer.char_class == DIGIT: # 수가 끝날 때까지
                self.add_char()
                self.get_char()
            g.next_token = CONST # 하나의 lexeme으로 인식 후 Constant임을 저장.
            g.const_num += 1

        # 변수, 상수 외의 lexeme 처리
        elif LexicalAnalyzer.char_class == UNKNOWN: 
            self.lookup(LexicalAnalyzer.next_char)
            self.get_char()
            self.get_non_blank()
            if LexicalAnalyzer.char_class == UNKNOWN and g.next_token == ASSIGN_OP:
                self.lookup(LexicalAnalyzer.next_char)
                self.get_char()
        else :
            g.next_token = EOF
            g.lexeme = "EOF"
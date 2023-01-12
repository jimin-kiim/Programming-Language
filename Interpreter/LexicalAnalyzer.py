from constants import *
import global_variables as g

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
        if character == "{":
            self.add_char()
            g.next_token = LEFT_BRACE
            g.token_string = ''.join(g.lexeme)

        elif character == "}":
            self.add_char()
            g.next_token = RIGHT_BRACE
            g.token_string = ''.join(g.lexeme)

        elif character == "_":
            self.add_char()
            g.next_token = UNDER_SCORE
            g.token_string = ''.join(g.lexeme)

        elif character == ",":
            self.add_char()
            g.next_token = COMMA
            g.token_string = ''.join(g.lexeme)

        elif character == ";":
            self.add_char()
            g.next_token = SEMI_COLON
            g.token_string = ''.join(g.lexeme)
            
        else:
            self.add_char()
            g.next_token = "\0"
            g.token_string = ''.join(g.lexeme)

    def lexical(self):
        g.lexeme = []
        self.get_non_blank()

        # identifiers and reserved words
        if LexicalAnalyzer.char_class == LETTER: # when the lexeme starts with Letter
            self.add_char()
            self.get_char()
            while LexicalAnalyzer.char_class == LETTER or LexicalAnalyzer.char_class == DIGIT : # LETTER나 DIGIT로 이루어진 부분까지 
                self.add_char()
                self.get_char()
            g.token_string = ''.join(g.lexeme)
            if g.token_string == 'variable' :
                g.next_token = VARIABLE
            elif g.token_string == 'call':
                g.next_token = CALL
            elif g.token_string == 'print':
                self.lookup(LexicalAnalyzer.next_char)
                if g.next_token == UNDER_SCORE:
                    self.get_char()
                    while LexicalAnalyzer.char_class == LETTER or LexicalAnalyzer.char_class == DIGIT:
                        self.add_char()
                        self.get_char()
                    g.token_string = ''.join(g.lexeme)
                    if g.token_string == 'print_ari' :
                        g.next_token = PRINT_ARI
            else: 
                g.next_token = IDENT  
        
        # curly braces, semi colon, comma
        elif LexicalAnalyzer.char_class == UNKNOWN: 
            self.lookup(LexicalAnalyzer.next_char)
            self.get_char()
                
        else :
            g.next_token = EOF
            g.lexeme = EOF
            g.token_string = EOF
        print_lexeme = ''.join(g.lexeme)
        # print("Next token is", g.next_token, "Next lexeme is", print_lexeme )
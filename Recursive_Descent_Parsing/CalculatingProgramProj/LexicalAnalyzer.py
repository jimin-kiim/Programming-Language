from constants import *
import global_variables as g

# character를 한 자를 읽어 charater의 Type을 알아냅니다. 
def get_char():
    # print(">>>>>GET_CHAR next_token",g.next_token )
    g.next_char = g.input[g.index]
    g.index += 1 # 다음 번에 함수 실행 시 현재 character의 다음 character를 읽을 수 있도록. 
    if  g.next_char != "\0" :
        if g.next_char.isalpha():
            g.char_class = LETTER
        elif g.next_char.isdigit():
            g.char_class = DIGIT
        else:
            g.char_class = UNKNOWN
    else:
        g.char_class = EOF

# UNKNOWN으로 판별난 character가 빈칸은 아니였는지 다시 체크 후 빈칸이었다면 다시 체크
def get_non_blank():
    # print(">>>>>next_char",g.next_char,g.char_class)
    while g.next_char.isspace():
        get_char()
        # print(">>>>NEXT_CHAR",g.next_char,g.char_class)

def add_char():
    g.lexeme.append(g.next_char)

def lookup(character):
    if character == "(":
        add_char()
        g.next_token = LEFT_PAREN

    elif character == ")":
        add_char()
        g.next_token = RIGHT_PAREN

    elif character == "+":
        add_char()
        g.next_token = ADD_OP

    elif character == "-":
        add_char()
        g.next_token = SUB_OP

    elif character == "*":
        add_char()
        g.next_token = MULT_OP

    elif character == "/":
        add_char()
        g.next_token = DIV_OP

    elif character == ":":
        add_char()
        g.next_token = ASSIGN_OP

    elif character == "=":
        add_char()
        g.next_token = ASSIGN_OP

    elif character == ";":
        add_char()
        g.next_token = SEMI_COLON
        
    else:
        print(">>>>ELSE",character)
        add_char()
        g.next_token = "\0"
    return g.next_token

def lexical():
    g.lexeme = []
    get_non_blank()

    # lexeme이 LETTER로 시작한다면 
    if g.char_class == LETTER:
        add_char()
        get_char()

        # LETTER나 DIGIT로 이루어진 부분까지 
        while g.char_class == LETTER or g.char_class == DIGIT:
            add_char()
            get_char()
        
        # 하나의 lexeme으로 인식 후 이의 타입이 Identifier 임을 저장. 
        g.next_token = IDENT
    
    # 숫자로 시작한다면 
    elif g.char_class == DIGIT:
        add_char()
        get_char()

        # 수가 끝날 때까지
        while g.char_class == DIGIT:
            add_char()
            get_char()

        # 하나의 lexeme으로 인식 후 Constant임을 저장.
        g.next_token = CONST

    # 변수, 상수 외의 lexeme 처리
    elif g.char_class == UNKNOWN:
        lookup(g.next_char)
        get_char()
        if g.char_class == UNKNOWN:
            # lookup(g.next_char)
            lookup(g.next_char)
            get_char()
    else : # g.char_class == EOF
        # print(">>>>ELSE",g.next_char)
        g.next_token = EOF
        g.lexeme = "EOF"
    print_lexeme = ''.join(g.lexeme)
    # print(">>>>ABOVE PRINT",g.next_char)
    print("Next token is", g.next_token, "Next lexeme is", print_lexeme )
    return g.next_token
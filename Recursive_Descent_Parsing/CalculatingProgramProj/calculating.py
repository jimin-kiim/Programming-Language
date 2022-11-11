from Ident import *

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
 
def infixToPostfix(expression): 
    stack = [] # initialization of empty stack
    output = []
    for token in expression:
        if token not in Operators:  # if an operand append in postfix expression
            output.append(token) 
        elif token=='(':  # else Operators push onto stack
            stack.append('(')
        elif token==')':
            while stack and stack[-1]!= '(':
                output.append(stack.pop())
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and Priority[token]<=Priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate(text):
    if len(text) == 1:
        return text[0]
    text = infixToPostfix(text)
    print(text)
    s = list()
    
    for symbol in text:
        # if symbol.isdecimal():
        #     s.append(int(symbol))
        # if symbol.type == Ident:
        #     s.append(int(symbol.value))
        
        if isinstance(symbol, Ident):
            print(symbol.name)
            s.append(int(symbol.value))
        elif symbol.isdecimal():
            s.append(int(symbol))
        # elif not s.is_empty():
        elif len(s) != 0:
            plus = None
            if symbol == "+":
                plus = s.pop() + s.pop()
            elif symbol == "-":
                plus = s.pop() - s.pop()
            elif symbol == "*":
                plus = s.pop() * s.pop()
            elif symbol == "/":
                plus = s.pop() / s.pop()
            else:
                pass
            if plus is not None:
                print(">>>>>>>",symbol)
                s.append(plus)
        else:
            raise Exception("unknown value %s"%symbol)
    return s.pop()
    # return 50
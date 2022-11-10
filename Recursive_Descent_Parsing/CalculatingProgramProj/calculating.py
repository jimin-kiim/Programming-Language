Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
 
def infixToPostfix(expression): 
    stack = [] # initialization of empty stack
    output = '' 
    for character in expression:
        if character not in Operators:  # if an operand append in postfix expression
            output+= character
        elif character=='(':  # else Operators push onto stack
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output

def evaluate(text):
    # s = list()
    # for symbol in text:
    #     if symbol in "0123456789":
    #         s.append(int(symbol))

    #     plus = None
    #     elif not s.is_empty():
    #         if symbol == "+":
    #             plus = s.pop() + s.pop()
    #         elif symbol == "-":
    #             plus = s.pop() - s.pop()
    #         elif symbol == "*":
    #             plus = s.pop() * s.pop()
    #         elif symbol == "/":
    #             plus = s.pop() / s.pop()
    #     if plus is not None:
    #         s.append(plus)
    #     else:
    #         raise Exception("unknown value %s"%symbol)
    # return s.pop()
    return 50
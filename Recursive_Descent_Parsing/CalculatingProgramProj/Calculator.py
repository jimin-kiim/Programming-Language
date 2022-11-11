from Ident import *

class Calculator:
    Operators = set(['+', '-', '*', '/', '(', ')', '^'])
    Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def infixToPostfix(self,expression): 
        stack = [] 
        output = []
        for token in expression:
            if token not in Calculator.Operators: 
                output.append(token) 
            elif token == '(': 
                stack.append('(')
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else: 
                while stack and stack[-1] != '(' and Calculator.Priority[token] <= Calculator.Priority[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate(self,text):
        if len(text) == 1:
            return text[0]
        text = self.infixToPostfix(text)
        s = list()
        
        for symbol in text:
            if isinstance(symbol, Ident):
                s.append(int(symbol.value))
            elif symbol.isdecimal():
                s.append(int(symbol))
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
                    s.append(plus)
            else:
                raise Exception("unknown value %s"%symbol)
        return s.pop()
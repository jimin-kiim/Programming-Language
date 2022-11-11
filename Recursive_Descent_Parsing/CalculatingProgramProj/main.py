from constants import *
import global_variables as g
from FileOpener import *
from Lexer import *
from ParsingProgram import *

def main():
    g.input = read_file()
    g.input = g.input.replace("\n"," ")
    g.input += "\0"
    lexer = Lexer()
    parser = ParsingProgram()
    lexer.get_char()
    lexer.lexical()
    parser.program()
    while(g.next_token!=EOF):
        lexer.lexical()

if __name__ == "__main__":
    main()
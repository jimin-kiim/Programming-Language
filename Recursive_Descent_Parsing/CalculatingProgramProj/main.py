from constants import *
import global_variables as g
from FileProcesor import *
from Lexer import *
from ParsingProgram import *

def main():
    file_processor = FileProcesor()
    lexer = Lexer()
    parser = ParsingProgram()

    g.input = file_processor.read_file()
    
    lexer.get_char()
    lexer.lexical()
    parser.program()
    while(g.next_token!=EOF):
        lexer.lexical()

if __name__ == "__main__":
    main()
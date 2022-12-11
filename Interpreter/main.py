from constants import *
import global_variables as g
from FileProcesor import *
from LexicalAnalyzer import *
from ParsingProgram import *

def main():
    file_processor = FileProcesor()
    lexical_analyzer = LexicalAnalyzer()
    parser = ParsingProgram()

    g.input = file_processor.read_file()
    
    lexical_analyzer.get_char()
    lexical_analyzer.lexical()
    parser.program()
    while(g.next_token!=EOF):
        lexical_analyzer.lexical()

if __name__ == "__main__":
    main()
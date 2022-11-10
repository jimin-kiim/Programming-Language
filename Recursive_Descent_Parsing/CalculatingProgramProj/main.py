from constants import *
import global_variables as g
from FileOpener import *
from LexicalAnalyzer import *
from RecursiveFunctions import *

def main():
    g.input = read_file()
    g.input = g.input.replace("\n"," ")
    g.input += "\0"
    get_char()
    lexical()
    program()
    while(g.next_token!=EOF):
        lexical()

if __name__ == "__main__":
    main()
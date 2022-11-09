from constants import *
# from global_variables import *
import global_variables as g
from FileOpener import *
from LexicalAnalyzer import *
from RecursiveFunctions import *

def main():
    # global input
    g.input = read_file()
    g.input = g.input.replace("\n"," ")
    g.input += "\0"
    print(">>>>>INPUT",g.input)
    get_char()
    lexical()
    program()
    while(g.next_token!="EOF"):
        lexical()

if __name__ == "__main__":
    main()
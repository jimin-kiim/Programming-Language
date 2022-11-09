from constants import *
from global_variables import *
from FileOpener import *
from LexicalAnalyzer import *
from Parser import *

def main():
    global input 
    input = read_file()
    input += "\0"
    get_char()

    lex()
    expression()
    while(next_token!="EOF"):
        lex()

if __name__ == "__main__":
    main()
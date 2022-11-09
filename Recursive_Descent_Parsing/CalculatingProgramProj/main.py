from constants import *
from global_variables import *
from FileOpener import *
from LexicalAnalyzer import *
from RecursiveFunctions import *

def main():
    global input 
    input = read_file()
    input = input.replace("\n"," ")
    input += "\0"
    print(">>>>>INPUT",input)
    get_char()
    lexical()
    program()
    while(next_token!="EOF"):
        lexical()

if __name__ == "__main__":
    main()
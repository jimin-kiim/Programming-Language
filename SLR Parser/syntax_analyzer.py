from parser import *
import sys

def read_file():
    string = ""
    input_file = sys.argv[1]
    with open(input_file,'r') as filereader:
        for row in filereader:
            string += row
    
    return string 

def main():
    global input 
    input = read_file()
    input += ' $'
    parse(input)

if __name__ == "__main__":
    main()
from parser import *
import sys

def read_file(args):
    string = ""
    input_file = args[0]
    with open(input_file,'r') as filereader:
        for row in filereader:
            string += row
    return string 

def main(args):
    global input 
    input = read_file(args)
    input += ' $'
    parse(input)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
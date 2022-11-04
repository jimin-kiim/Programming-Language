import re
import sys
import pandas as pd

def cal_follow(s, productions, first):
    follow = set()
    if len(s)!=1 :
        return {}
    if(s == list(productions.keys())[0]):
        follow.add('$') 
    
    for i in productions:
        for j in range(len(productions[i])):
            if(s in productions[i][j]):
                idx = productions[i][j].index(s)
                
                if(idx == len(productions[i][j])-1):
                    if(productions[i][j][idx] == i):
                        break
                    else:
                        f = cal_follow(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while(idx != len(productions[i][j]) - 1):
                        idx += 1
                        if(not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = cal_first(productions[i][j][idx], productions)
                            
                            if('ε' not in f):
                                for x in f:
                                    follow.add(x)
                                break
                            elif('ε' in f and idx != len(productions[i][j])-1):
                                f.remove('ε')
                                for k in f:
                                    follow.add(k)
                            
                            elif('ε' in f and idx == len(productions[i][j])-1):
                                f.remove('ε')
                                for k in f:
                                    follow.add(k)
                                
                                f = cal_follow(i, productions, first)
                                for x in f:
                                    follow.add(x)
                            
    return follow
   
def cal_first(s, productions):
    
    first = set()
    
    for i in range(len(productions[s])):
        
        for j in range(len(productions[s][i])):
            
            c = productions[s][i][j]
            
            if(c.isupper()):
                f = cal_first(c, productions)
                if('ε' not in f):
                    for k in f:
                        first.add(k)
                    break
                else:
                    if(j == len(productions[s][i])-1):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('ε')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break
                
    return first

def parsing_table(productions, first, follow):
    
    print("\nParsing Table\n")

    table = {}
    for key in productions:
        for value in productions[key]:
            val = ''.join(value)
            if val != 'ε':
                for element in first[key]:
                    if(element != 'ε'):
                        if(not val[0].isupper()) :
                            if(element in val):
                                table[key, element] = val
                            else:
                                pass
                        else:
                            table[key, element] = val
            else:
                for element in follow[key]:
                    table[key, element] = val

    for key,val in table.items():
        print(key,"=>",val)

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]


    print("\n")
    print("\nParsing Table in matrix form\n")
    print(pd.DataFrame(new_table).fillna('-'))
    print("\n")
    
    return table


def check_validity(string, start, table):
    
    accepted = True
    splitted_string = re.split(" |\n", string)
    # print(splited_string)
    input_string = []
    for i in splitted_string:
        if (i == "" or i == None or i == '\n' or i == " " or i == "→" or i == "_"):
            pass
        else:
            input_string.append(i)
    # print(m)
    input_string.append('$')
    print(input_string)
    stack = []
    
    stack.append('$')
    stack.append(start)
    
    idx = 0
    print("Stack\t\tInput\t\tMoves") 
    while (len(stack) > 0):
        
        top = stack[-1]
        print(f"Top => {top}")
        
        curr_string = input_string[idx]
        print(f"Current input => {curr_string}")
    
        if top == curr_string:
            stack.pop()
            idx += 1
        
        else:
            key = (top, curr_string)
            print(f"Key => {key}")
            if key not in table:
                accepted = False
                break
            
            value = table[key]
            if value != 'ε':
                value = value[::-1]
                value = list(value)
                
                stack.pop()
                
                for ele in value:
                    stack.append(ele)
            
            else:
                stack.pop()
    
    if accepted:
        print("String accepted")
    else:
        print("String not accepted")
        
def main():
    productions = {}
    grammar = open("grammar.txt", "r")
    
    first = {}
    follow = {}
    table = {}
    
    start = ""
    
    for prod in grammar:
        l = re.split(" |\n", prod)
        m = []
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "→" or i == "_"):
                pass
            else:
                m.append(i)
        left_prod = m.pop(0)
        right_prod = []
        t = []
        
        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                right_prod.append(t)
                t = []
        
        right_prod.append(t)
        productions[left_prod] = right_prod
        
        if(start == ""):
            start = left_prod
      
    print("*****GRAMMAR*****")    
    for lhs, rhs in productions.items():
        print(lhs, ":" , rhs)
    print("")
    
    for s in productions.keys():
        first[s] = cal_first(s, productions)
    
    print("*****FIRST*****")
    for lhs, rhs in first.items():
        print(lhs, ":" , rhs)
    
    print("")
    
    for lhs in productions:
        follow[lhs] = set()
    
    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)
    
    print("*****FOLLOW*****")
    for lhs, rhs in follow.items():
        print(lhs, ":" , rhs)
    
    table = parsing_table(productions, first, follow)
    # string = input("Enter a string to check its valididty : ")
    string = read_file()
    check_validity(string, start, table)
    grammar.close()

def read_file():
  string = ""
  input_file = sys.argv[1]
  with open(input_file,'r') as filereader:
      for row in filereader:
        string += row
  return string 

if __name__ == "__main__":
    main()

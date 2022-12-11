import sys

class FileProcesor:
    def read_file(self):
        string = ""
        input_file = sys.argv[1]
        with open(input_file,'r') as filereader:
            for row in filereader:
                string += row
        
        string = self.refine_string(string)
        return string 
    
    def refine_string(self, string):
        string = string.replace("\n"," ")
        string += "\0"

        return string

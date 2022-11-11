input = ""
next_token = ""
index = 0
next_char = 0
char_class = 0
lexeme = []

ident_num = 0
const_num = 0
op_num = 0

temp = None
ident = None
identifiers = set()
valid_identifiers = {}
defined_identifiers = {}
defined_ident_names = []
identifier_names = set()

# stack = []
refined_expression = []
warning = None
error = None
should_be_calculated = True
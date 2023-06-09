parsing_table = [
    {'vtype':'s2', 'VDECL':1 },
    {'vtype':'s6', 'class': 's7', '$':'r3', 'CODE':3, 'VDECL':1, 'FDECL':4, 'CDECL':5},
    {'id':'s8','ASSIGN':9},
    {'$':'acc'},
    {'vtype':'s6', 'class':'s7', '$':'r3', 'CODE':10, 'VDECL':1, 'FDECL':4,'CDECL':5},
    {'vtype':'s6', 'class':'s7', '$':'r3', 'CODE':11, 'VDECL':1, 'FDECL':4,'CDECL':5},
    {'id':'s12', 'ASSIGN':9},
    {'id':'s13'},
    {'semi':'s14', 'assign':'s15'},
    {'semi':'s16'},
    {'$':'r1'},
    {'$':'r2'},
    {'semi':'s14', 'assign':'s15', 'lparen':'s17'},
    {'lbrace':'s18'}, 
    {'vtype':'r4', 'id':'r4', 'rbrace':'r4', 'if':'r4', 'while':'r4', 'return':'r4', 'class':'r4', '$':'r4'},
    {'id':'s27', 'literal':'s21', 'character':'s22', 'boolstr':'s23', 'lparen':'s25', 'num':'s28', 'RHS':19, 'EXPR':20, 'T':24, 'F':26},
    {'vtype':'r5', 'id':'r5','rbrace':'r5', 'if':'r5', 'while':'r5', 'return':'r5', 'class':'r5', '$':'r5'},
    {'vtype':'s30', 'rparen':'r20', 'ARG':29},
    {'vtype':'s6', 'rbrace':'r37', 'VDECL':32, 'FDECL':33, 'ODECL':31},
    {'semi':'r6'},
    {'semi':'r7'},
    {'semi':'r8'},
    {'semi':'r9'},
    {'semi':'r10'},
    {'semi': 'r12', 'addsub':'s34', 'rparen':'r12'},
    {'id':'s27','lparen':'s25', 'num':'s28', 'EXPR':35, 'T':24, 'F':26},
    {'semi':'r15', 'addsub':'r15', 'multdiv':'r36', 'rparen': 'r15'},
    {'semi':'r16', 'addsub':'r16', 'multdiv':'r16', 'rparen':'r16'},
    {'semi':'r17', 'addsub':'r17', 'multdiv':'r17', 'rparen':'r17'},
    {'rparen':'s37'},
    {'id':'s38'},
    {'rbrace':'s39'},
    {'vtype':'s6', 'rbrace':'r37', 'CODE':32, 'FDECL':33, 'ODECL':40},
    {'vtype':'s6', 'rbrace':'r37', 'CODE':32, 'FDECL':33, 'ODECL':41},
    {'semi':'s27', 'lparen':'s25', 'num':'s28', 'RHS':42, 'T':24, 'F':26},
    {'rparen':'s43'},
    {'id':'s27', 'num':'s28', 'T':44, 'F':26},
    {'lbrace':'s45'},
    {'rparen':'r22', 'comma':'s47', 'MOREARGS':46},
    {'vtype':'r34', 'class':'r34', '$':'r34'},
    {'rbrace':'s35'},
    {'rbrace':'s36'},
    {'semi':'r11', 'rparen':'r11'},
    {'semi':'r14', 'rparen':'r14'},
    {'semi':'r13', 'addsub':'r13', 'rparen':'r13'},
    {'vtype':'s2', 'id':'s54', 'rbrace':'r24', 'if':'s52', 'while':'s53', 'return':'r24', 'VDECL':50, 'ASSIGN':51, 'BLOCK':48, 'STMT':49},
    {'rparen':'r19'},
    {'vtype':'s55'},
    {'return':'s57', 'RETURN':56},
    {'vtype':'s2', 'id':'s54', 'rbrace':'r24', 'if':'s52', 'while':'s53', 'return':'r24', 'VDECL':50, 'ASSIGN':51, 'BLOCK':58, 'STMT':49},
    {'vtype':'s25', 'id':'s25', 'rbrace':'r25', 'if':'s25', 'while':'s25', 'return':'r25'},
    {'semi':'s59'},
    {'lparen':'s60'},
    {'lparen':'s61'},
    {'assign':'s15'},
    {'id':'s62'},
    {'rbrace':'s63'},
    {'id':'s27', 'literal':'s21', 'character':'s22', 'boolstr':'s23', 'lparen':'s25', 'num':'s28', 'RHS':64, 'EXPR':20, 'T':24, 'F':26},
    {'rbrace':'r23', 'return':'r23'},
    {'vtype':'r26', 'id':'r26', 'rbrace':'r26', 'if':'r26', 'while':'r26', 'return':'r26'},
    {'boolstr':'s66', 'COND':65},
    {'boolstr':'s66', 'COND':67},
    {'rparen':'r22', 'comma':'s47', 'MOREARGS':68},
    {'vtype':'r18', 'rbrace':'r18', 'class':'r18', '$':'r18'},
    {'semi':'s69'},
    {'rparen':'s70', 'comp':'s71'},
    {'rparen':'r30', 'comp':'r30'},
    {'rparen':'s72', 'comp':'s71'},
    {'rparen':'r21'},
    {'rbrace':'r33'},
    {'lbrace':'s73'},
    {'boolstr':'s74'},
    {'lbrace':'s75'},
    {'vtype':'s2', 'id':'s54', 'rbrace':'r24', 'if':'s52', 'while':'s53', 'return':'r24', 'VDECL':50, 'ASSIGN':51, 'BLOCK':76, 'STMT':49},
    {'rparen':'r29', 'comp':'r29'},
    {'vtype':'s2', 'id':'s54', 'rbrace':'r24', 'if':'s52', 'while':'s53', 'return':'r24', 'VDECL':50, 'ASSIGN':51, 'BLOCK':77, 'STMT':49},
    {'rbrace':'s78'},
    {'rbrace':'s79'},
    {'vtype':'r32', 'id':'r32', 'rbrace':'r32', 'if':'r32', 'while':'r32', 'else':'s81', 'return':'r32', 'ELSE':80},
    {'vtype':'r28', 'id':'r28', 'rbrace':'r28', 'if':'r28', 'while':'r28', 'return':'r28'},
    {'vtype':'r27', 'id':'r27', 'rbrace':'r27', 'if':'r27', 'while':'r27', 'return':'r27'},
    {'lbrace':'s82'},
    {'vtype':'s2', 'id':'s54', 'rbrace':'r24', 'if':'s52', 'while':'s53', 'return':'r24', 'VDECL':50, 'ASSIGN':51, 'BLOCK':83, 'STMT':49},
    {'rbrace':'s84'},
    {'vtype':'r31', 'id':'r31', 'rbrace':'r31', 'if':'r31', 'while':'r31', 'return':'r31'}
]

import ply.yacc as yacc
from pl3 import *

    
symboltable = {}

lableofindex = {0:0}
out_of_file = open("file_out.txt", "w")
halghe= {}
con_if = []
 

class Stack():
    def __init__(self):
        self.inp=[]
    def push(self, input_st):
        self.inp.append(input_st)
    def pop(self):
        return self.inp.pop()
    def isEmpty(self):
        return (self.inp == [])
class new_lable():
    def __init__(self):
        self.index_lable = 0
    def indexplus(self):
        self.index_lable = self.index_lable + 1
        return self.index_lable
flagst = Stack()
flag_temp = Stack()
index_of_lable= Stack()
def p_iffunction(p):
    """S : IFY S
    | IFY
    | WHILEY
    | WHILEY S
    | ASSIGN S
    | ASSIGN
    | PRINTY
    | PRINTY S"""
    p[0]=p[1]
    print("in s",p[1])
    print("********************************\n")
def p_ifY(p):
    'IFY : IF Xif CONDITION DONOGHTEH LBRAC S1 RBRAC TF1'
    print ("in ify", p[4])
   
def p_TF1(p):
    'TF1 : ELIF XELIF CONDITION DONOGHTEH LBRAC S1 RBRAC TF1'
def p_TF1_2(p):
    'TF1 : '
    out_of_file.write(index_of_lable.pop())
def p_XELIF(p):
    'XELIF : '
    out_of_file.write(index_of_lable.pop())

def p_xif(p):
    'Xif :'
    con_if.append(True)
    print("con_if is true", con_if)

def p_s1if(p):
    """S1 : IFY S1
    | IFY"""

def p_s1while(p):
    """S1 : WHILEY S1
    | WHILEY"""
def p_s1assign(p):
    """S1 : ASSIGN S1
    | ASSIGN"""
def p_s1print(p):
    """S1 : PRINTY S1
    | PRINTY"""
def p_printstr(p):
    'PRINTY : PRINT LP STR RP'
    if not flag_temp.isEmpty():
        if flag_temp.pop():
            print("flag_temp dar assignment is true")
            if not flagst.isEmpty():
                flagst.pop()
                flagst.push(True)
                z=flagst.pop()
                print("flagst dar assignment ", z)
                flagst.push(z)
            flag_temp.push(True)
    if flag_temp.isEmpty():
        length = len(p[3])
        input_string = "output " + p[3][1:length-1] + "\n"
        out_of_file.write(input_string)
    elif flag_temp.pop():
        length = len(p[3])
        input_string = "output " + p[3][1:length-1] + "\n"
        out_of_file.write(input_string)
        flag_temp.push(True)
def p_printID(p):
    'PRINTY : PRINT LP ID RP'
    if not flag_temp.isEmpty():
        if flag_temp.pop():
            print("flag_temp dar assignment is true")
            if not flagst.isEmpty():
                flagst.pop()
                flagst.push(True)
                z=flagst.pop()
                print("flagst dar assignment ", z)
                flagst.push(z)
            flag_temp.push(True)
    if flag_temp.isEmpty():
        if p[3] in symboltable.keys():
            print(p[3], " = ", symboltable[p[3]])
            input_string = "output " + str(p[3]) + "\n"
            out_of_file.write(input_string)
        else:
            Error = "Error_print_ID : " + p[3] + " not defined..." + "\n"
            out_of_file.write(Error)
            print("Error_print_ID : ", p[3], " not defined...")
    elif flag_temp.pop():
        if p[3] in symboltable.keys():
            print(p[3], " = ", symboltable[p[3]])
            input_string = "output " + str(p[3]) + "\n"
            out_of_file.write(input_string)
        else:
            Error = "Error_print_ID : " + p[3] + " not defined..." + "\n"
            out_of_file.write(Error)
            print("Error_print_ID : ", p[3], " not defined...")
            flag_temp.push(True)
def p_print(p):
    'PRINTY : PRINT LP NUM RP'
    if not flag_temp.isEmpty():
        if flag_temp.pop():
            print("flag_temp dar assignment is true")
            if not flagst.isEmpty():
                flagst.pop()
                flagst.push(True)
                z=flagst.pop()
                print("flagst dar assignment ", z)
                flagst.push(z)
            flag_temp.push(True)
    if flag_temp.isEmpty():
        input_string = "output " + str(p[3]) + "\n"
        out_of_file.write(str(p[3]))
    elif flag_temp.pop():
        input_string = "output " + str(p[3]) + "\n"
        out_of_file.write(str(p[3]))
        flag_temp.push(True)
def p_printl(p):
    'PRINTY : PRINT LP RP'
    if not flag_temp.isEmpty():
        if flag_temp.pop():
            print("flag_temp dar assignment is true")
            if not flagst.isEmpty():
                flagst.pop()
                flagst.push(True)
                z=flagst.pop()
                print("flagst dar assignment ", z)
                flagst.push(z)
            flag_temp.push(True)
    if flag_temp.isEmpty():
        input_string = "output \\n"
        out_of_file.write("\n")
#        print()
    elif flag_temp.pop():
        input_string = "output \\n"
        out_of_file.write("\n")
        flag_temp.push(True)
def p_input(p):
    'INPUTY : INPUT LP STR RP'
    input_string = "output " + str(p[3][1:len(p[3]-1)]) + "\n" + "input"
    out_of_file.write(input_string)
#   input(p[3])
def p_input2(p):
    'INPUTY : INPUT LP RP'
    input_string = "input"
    out_of_file.write(input_string)
def p_while(p):
    'WHILEY : WHILE XWhile CONDITION DONOGHTEH LBRAC S1 RBRAC'
    m = index_of_lable.pop()
    Lp ="halghe lbl" + str(index_of_lable.pop()) + "\n"
    out_of_file.write(Lp)
    out_of_file.write(m)
    print("in while")
def p_XWhile(p):
    'XWhile : '
    #
    lbl1 = "lbl" + str(lableofindex[0]+1) + "\n"
    index_of_lable.push(lableofindex[0]+1)
    out_of_file.write(lbl1)
    lableofindex[0] = lableofindex[0] + 1
def p_varid(p):
    'VAR : ID '
    p[0] = p[1]
def p_varnum(p):
    'VAR : NUM'
    p[0] = p[1]
def p_assignment2e(p):
    'ASSIGN2 : E'
    print("in assign2e", p[1])
    p[0]=p[1]
def p_assignment(p):
    'ASSIGN : ID EN E'
    if not flag_temp.isEmpty():
        if flag_temp.pop():
            print("flag_temp dar assignment is true")
            if not flagst.isEmpty():
                flagst.pop()
                flagst.push(True)
                z=flagst.pop()
                print("flagst dar assignment ", z)
                flagst.push(z)
            flag_temp.push(True)
        else: flag_temp.push(False)
    if flag_temp.isEmpty():
        if type(p[3]) == float:
            symboltable[p[1]] = p[3]
           
        elif p[3] in symboltable.keys():
            symboltable[p[1]] = symboltable[p[3]]
            
        else:
            print("Error_cnd_Empty : ", p[3], " not defined...")
        print(symboltable)
        print("in assign to if cnd empty")
    elif flag_temp.pop():
        if type(p[3]) == float:
            symboltable[p[1]] = p[3]
            
        elif p[3] in symboltable.keys():
            symboltable[p[1]] = symboltable[p[3]]
           
        else:
            print("Error_stmt_cnd : ", p[3], " not defined...")
        print(symboltable)
        print("in assign, to flagst o flag_temp" )
        flag_temp.push(True)
    else:
        flag_temp.push(False)
        flagst.push(False)
    t1 = "mov " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(t1)
def p_assignment2input(p):
    'ASSIGN2 : INPUTY'
    p[0]=p[1]
def p_conditioneal(p):
    'CONDITION : ID EQUAL VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] == p[3]:
            p[0] = True
        else:
            p[0] = False
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] == symboltable[p[3]]:
            print ("in 2, if", p[3])
            p[0] = True
        else:
            p[0] = False
            print ("in 2, Else",p[0], p[1], p[2], p[3])
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "jne lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_conditionbig(p):
    'CONDITION : VAR B VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] > p[3]:
            print ("in 1, if", p[3])
            p[0] = True
        else:
            p[0] = False
            print ("in 1, Else",p[0], p[1], p[2], p[3])
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] > symboltable[p[3]]:
            print ("in 2, if", p[3])
            p[0] = True
        else:
            p[0] = False
            print ("in 2, Else",p[0], p[1], p[2], p[3])
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    print(cmp)
    out_of_file.write(cmp)
    index_of_lable.push("lbl" + str(lableofindex[0]) + "\n")
    jmp = "jle lbl" + str(lableofindex[0]) +"\n"
    out_of_file.write(jmp)
    #con_if.pop()
def p_conditionsmaller(p):
    'CONDITION : VAR K VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] < p[3]:
            print ("in 1, if", p[3])
            p[0] = True
        else:
            p[0] = False
            print ("in 1, Else",p[0], p[1], p[2], p[3])
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] < symboltable[p[3]]:
            print ("in 2, if", p[3])
            p[0] = True
        else:
            p[0] = False
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "jge lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_conditionke(p):
    'CONDITION : VAR KE VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] <= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] <= symboltable[p[3]]:
            p[0] = True
        else:
            p[0] = False
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "jg lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_conditionbe(p):
    'CONDITION : VAR BE VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] >= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] >= symboltable[p[3]]:

            p[0] = True
        else:
            p[0] = False
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "jl lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_conditionnoteq(p):
    'CONDITION : VAR NOTEQUAL VAR'
    if p[1] not in symboltable.keys():
        print("Error : ", p[1], "not defined...")
    elif type(p[3]) == float :
        if symboltable[p[1]] != p[3]:
            p[0] = True
        else:
            p[0] = False
    elif type(p[3]) == str and p[3] in symboltable.keys():
        if symboltable[p[1]] != symboltable[p[3]]:
            p[0] = True
        else:
            p[0] = False
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "je lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_conditioninput(p):
    'CONDITION : INPUTY'
    if p[1]:
        p[0] = True
    else:
        p[0] = False
    flagst.push(False)
    flag_temp.push(p[0])
    newtemp = lableofindex[0]
    lbl ="lbl" + str(newtemp) + "\n"
    if newtemp in halghe.keys():
        print("in halghe.keys", newtemp)
        halghe[newtemp] = halghe[newtemp] + 1
    else:
        print("not in halghe.keys", newtemp)
        halghe[newtemp] = 0
    lableofindex[0] = newtemp + 1
    print("halghe[newtemp]", halghe[newtemp])
    print(con_if)
    cmp = "cmp " + str(p[1]) + ", " + str(p[3]) + "\n"
    out_of_file.write(cmp)
    jmp = "jge lbl" + str(lableofindex[0]) +"\n"
    index_of_lable.push("lbl"+str(lableofindex[0]) +'\n')
    out_of_file.write(jmp)
def p_accountplus(p):
    'E : E PLUS T'
    if type(p[1]) == str and p[1] in symboltable.keys():
        if type(p[3]) == str and p[3] in symboltable.keys():
            p[0]=symboltable[p[1]] + symboltable[p[3]]
            t1 = "add " + str(p[1]) + ", " + str(p[3]) +"\n"
            out_of_file.write(t1)
        elif type(p[3]) == float:
            p[0]=symboltable[p[1]] + p[3]
            t1 = "add " + str(p[1]) + ", " + str(p[3]) + "\n"
            out_of_file.write(t1)
    elif type(p[1]) == float and type(p[3]) == float:
        p[0] = p[1] + p[3]
        t1 = "add " + str(p[1]) + ", " + str(p[3]) + "\n"
        out_of_file.write(t1)
    print("in plus")

def p_accountminus(p):
    'E : E MINUS T'
    if type(p[1]) == str and p[1] in symboltable.keys():
        if type(p[3]) == str and p[3] in symboltable.keys():
            p[0]=symboltable[p[1]] - symboltable[p[3]]
            t1 = "sub " + str(p[1]) + ", " + str(p[3]) + "\n"
            out_of_file.write(t1)
        elif type(p[3]) == float:
            p[0]=symboltable[p[1]] - p[3]
            t1 = "sub " + str(p[1]) + ", " + str(p[3]) + "\n"
            out_of_file.write(t1)
    elif type(p[1]) == float and type(p[3]) == float:
        p[0] = p[1] - p[3]
        t1 = "sub " + str(p[1]) + ", " + str(p[3]) + "\n"
        out_of_file.write(t1)
def p_accountt(p):
    'E : T'
    p[0]=p[1]
def p_account2mul(p):
    'T : T MUL F'
    if type(p[1]) == str and p[1] in symboltable.keys():
        if type(p[3]) == str and p[3] in symboltable.keys():
            p[0]=symboltable[p[1]] * symboltable[p[3]]
            t1 = "mul " + str(p[1]) + ", " + str(p[3]) +"\n"
            out_of_file.write(t1)
        elif type(p[3]) == float:
            t1 = "mul " + str(p[1]) + ", " + str(p[3]) + "\n"
            p[0]=symboltable[p[1]] * p[3]
            out_of_file.write(t1)
    elif type(p[1]) == float and type(p[3]) == float:
        p[0] = p[1] * p[3]
        t1 = "mul " + str(p[1]) + ", " + str(p[3]) + "\n"
        out_of_file.write(t1)
def p_account2div(p):
    'T : T DIV F'
    if type(p[1]) == str and p[1] in symboltable.keys():
        if type(p[3]) == str and p[3] in symboltable.keys():
            p[0]=symboltable[p[1]] / symboltable[p[3]]
            t1 = "div " + str(p[1]) + ", " + str(p[3]) + "\n"
            out_of_file.write(t1)
        elif type(p[3]) == float:
            p[0]=symboltable[p[1]] / p[3]
            t1 = "div " + str(p[1]) + ", " + str(p[3]) + "\n"
            out_of_file.write(t1)
    elif type(p[1]) == float and type(p[3]) == float:
        p[0] = p[1] / p[3]
        t1 = "div " + str(p[1]) + ", " + str(p[3]) + "\n"
        out_of_file.write(t1)
def p_account2f(p):
    'T : F'
    p[0]=p[1]
def p_account3(p):
    'F : VAR'
    p[0]=p[1]
def p_accountp(p):
    'F : LP E RP'
    p[0]=p[2]
def p_error(p):
    print("Syntax error in input!")
    print(p)
    
input_test = open("test.txt", "r")
strings = input_test.readline()
print()
parser = yacc.yacc()
while strings:
    parser.parse(strings)
    strings = input_test.readline()



       



import ply.lex as lex
tokens=['NUM','PRINT','INPUT','IF','STR','WHILE','MINUS','PLUS','MUL','DIV','EQUAL','ELSE','ELIF',
        'ID','NOTEQUAL','EN','B','K','BE','KE','DEF','LP','RP','DOUBLECOT','DONOGHTEH','CAMA',
        'LBRAC', 'RBRAC', 'RETURN','newline']
t_ignore=' \t'
t_PLUS=r'\+'
t_MUL=r'\*'
t_DIV=r'\/'
#t_EQUAL=r'\=='
#t_B=r'\>'
#t_K=r'\<'
#t_BE=r'\>='
#t_KE=r'\<='
#t_NOTEQUAL=r'\!='
t_MINUS=r'\-'
#t_LP=r'\('
#t_RP=r'\)'
#t_DONOGHTEH=r'\:'
#t_CAMA=r'\,'

def t_error(t):
    print("Illegal Input = '", t.value)
    t.lexer.skip(1)
def t_RETURN(t):
    r'return'
    return t
#def t_DOUBLECOT(t):
#    r'\"'
#    return t
def t_RBRAC(t):
    r'\}'
    return t
def t_KE(t):
    r'\<='
    return t
def t_BE(t):
    r'\>='
    return t
def t_LBRAC(t):
    r'\{'
    return t
def t_K(t):
    r'\<'
    return t
def t_B(t):
    r'\>'
    return t
def t_CAMA(t):
    r'\,'
    return t
def t_DONOGHTEH(t):
    r'\:'
    return t
def t_NOTEQUAL(t):
    r'\!='
    return t
def t_EQUAL(t):
    r'\=='
    return t
def t_LP(t):
    r'\('
    return t
def t_RP(t):
    r'\)'
    return t
def t_EN(t):
    r'='
    print(t)
    return t
def t_NUM(t):
      r'[0-9]+(\.[0-9]+)?'
      t.value = float(t.value)
      return t
def t_PRINT(t):
      r'print'
      return t
def t_INPUT(t):
      r'input'
      return t
def t_IF(t):
      r'if'
      return t
def t_ELIF(t):
      r'elif'
      return t
def t_ELSE(t):
      r'else'
      return t
def t_WHILE(t):
      r'while'
      return t
def t_DEF(t):
      r'def'
      return t
def t_ID(t):
      r'[a-zA-Z][a-zA-Z0-9]*'
      return t
def t_STR(t):
      r'".*?"'
#     t.value = str(t.value)
      return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
lexer=lex.lex()
lexer.input("p=")
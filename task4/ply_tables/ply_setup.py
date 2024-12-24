import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'ID', 
    'NUMBER',
    'TRUE', 
    'FALSE', 
    'PLUS', 
    'MINUS', 
    'MUL', 
    'DIV', 
    'AND', 
    'OR', 
    'NOT', 
    'ASSIGN',
    'EQ', 
    'NEQ', 
    'LT', 
    'LE', 
    'GT', 
    'GE', 
    'LPAREN', 
    'RPAREN', 
    'LBRACE',
    'RBRACE',
    'COMMA'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'true':
        t.type = 'TRUE'
    elif t.value == 'false':
        t.type = 'FALSE'
    return t

t_NUMBER = r'[0-9]+'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_program(p):
    '''program : expression'''

def p_expression(p):
    '''expression : assignment
                  | logical_expr'''
    
def p_assignment(p):
    '''assignment : ID ASSIGN expression'''

def p_logical_expr(p):
    '''logical_expr : logical_expr OR logical_term
                    | logical_term'''

def p_logical_term(p):
    '''logical_term : logical_term AND logical_factor
                    | logical_factor'''

def p_logical_factor(p):
    '''logical_factor : NOT logical_factor
                      | relational_expr'''
    
def p_relational_expr(p):
    '''relational_expr : relational_expr EQ additive_expr
                       | relational_expr NEQ additive_expr
                       | relational_expr LT additive_expr
                       | relational_expr LE additive_expr
                       | relational_expr GT additive_expr
                       | relational_expr GE additive_expr
                       | additive_expr'''

def p_additive_expr(p):
    '''additive_expr : additive_expr PLUS multiplicative_expr
                     | additive_expr MINUS multiplicative_expr
                     | multiplicative_expr'''

def p_multiplicative_expr(p):
    '''multiplicative_expr : multiplicative_expr MUL unary_expr
                            | multiplicative_expr DIV unary_expr
                            | unary_expr'''

def p_unary_expr(p):
    '''unary_expr : MINUS unary_expr
                  | primary_expr'''

def p_primary_expr(p):
    '''primary_expr : LPAREN expression RPAREN
                    | ID
                    | NUMBER
                    | TRUE
                    | FALSE
                    | function_definition
                    | function_call'''

def p_function_definition(p):
    '''function_definition : ID LPAREN argument_list RPAREN LBRACE expression RBRACE'''

def p_function_call(p):
    '''function_call : ID LPAREN argument_list RPAREN'''

def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression'''

def p_error(p):
    print(f"Syntax error at '{p}'")

lexer = lex.lex()
parser = yacc.yacc(method="LALR")

program = """
x = 10
y = 20
z = x + y
foo(x, y)
function (z, x) { z * x > 0 }
"""

lexer.input(program)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)

"""
LexToken(ID,'x',1,1)
LexToken(ASSIGN,'=',1,3)
LexToken(NUMBER,'10',1,5)
LexToken(ID,'y',1,8)
LexToken(ASSIGN,'=',1,10)
LexToken(NUMBER,'20',1,12)
LexToken(ID,'z',1,15)
LexToken(ASSIGN,'=',1,17)
LexToken(ID,'x',1,19)
LexToken(PLUS,'+',1,21)
LexToken(ID,'y',1,23)
LexToken(ID,'foo',1,25)
LexToken(LPAREN,'(',1,28)
LexToken(ID,'x',1,29)
LexToken(COMMA,',',1,30)
LexToken(ID,'y',1,32)
LexToken(RPAREN,')',1,33)
LexToken(ID,'function',1,35)
LexToken(LPAREN,'(',1,44)
LexToken(ID,'z',1,45)
LexToken(COMMA,',',1,46)
LexToken(ID,'x',1,48)
LexToken(RPAREN,')',1,49)
LexToken(LBRACE,'{',1,51)
LexToken(ID,'z',1,53)
LexToken(MUL,'*',1,55)
LexToken(ID,'x',1,57)
LexToken(GT,'>',1,59)
LexToken(NUMBER,'0',1,61)
LexToken(RBRACE,'}',1,63)
"""

"""
ply parser contains calculated action and goto tables for my grammar, 
i just simply copy them from cli to const.py
"""
print(parser.action)
print(parser.goto)

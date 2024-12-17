import re


TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\b\d+\b'),
    ('TRUE',     r'\btrue\b'),
    ('FALSE',    r'\bfalse\b'),
    ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('AND',      r'&&'),
    ('OR',       r'\|\|'),
    ('NOT',      r'!'),
    ('ASSIGN',   r'='),
    ('EQ',       r'=='),
    ('NEQ',      r'!='),
    ('LT',       r'<'),
    ('LE',       r'<='),
    ('GT',       r'>'),
    ('GE',       r'>='),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('COMMA',    r','),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.')
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)

def tokenize(expression):
    split_expression = expression.split()

    tokens = []
    for word in split_expression:
        match = re.fullmatch(TOKEN_REGEX, word)

        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character {value!r}")
        else:
            tokens.append(kind)

    return tokens

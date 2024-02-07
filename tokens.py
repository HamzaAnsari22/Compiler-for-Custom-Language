RESERVED = 'RES'
INT = 'INT'
STRING = 'STRING'
ID = 'ID'
OP = 'OP'
COMMENT = 'COMMENT'
WS = 'WS'
ENDL = 'ENDL'
MINUS = 'MINUS'
TIMES = 'TIMES'
PLUS = 'PLUS'
EQUALS = 'EQUALS'
DIVIDE = 'DIVIDE'
token_exprs = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*',  None),
    (r'[Pp][lL][uU][sS]',  PLUS),
    (r'[Mm][iI][nN][uU][sS]',   MINUS),
    (r'[Tt][iI][mM][eE][sS]',  TIMES),
    (r'[Dd][iI][vV][iI][dD][eE]',   DIVIDE),
    (r'[Ee][qQ][uU][aA][lL][sS]',   EQUALS),
    (r'\d+', INT),(r'@', 'TERMINATOR'),
    (r'[a-z][A-Za-z0-9_]*', ID),
    (r'[^"]*',STRING),
    (r"[^']*",STRING)
]

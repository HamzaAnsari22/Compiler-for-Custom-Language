import sys
import collections
Token = collections.namedtuple('Token', ['type','value'])

class ExpressionTreeBuilder():
    def parse(self, tokline, line_num):
        self.line_num = line_num
        self.tokens = tokline
        self.tok = None 
        self.nexttok = None 
        self._advance() 
        if self.nexttok.type != 'INT':
            if not self.nexttok.type == 'ID':
                print('Error: Lines start with INT or ID, but got',
                    self.nexttok.type)
                sys.exit()
            else:
                return self.assign()
        return self.expr()
    def _advance(self):
        'Advance the current and next tokens'
        self.tok = self.nexttok
        if len(self.tokens) > 0: 
            self.nexttok = self.tokens[0]
            self.tokens = self.tokens[1:]
        else:
            self.nexttok = Token('None', 'null')
    def _accept(self,toktype):
        'Test (and consume) the next token if it matches token type'
        if self.nexttok:
            if self.nexttok.type == toktype:
                self._advance()
                return True
            else:
                return False
        else:
            return False
    def assign(self):
        'ASSIGN -> ID EQUALS EXP'
        val = self.nexttok.value
        if self._accept('ID'):
            if self._accept('EQUALS'):
                exp = self.expr()
                if self.nexttok.value!='@':
                    print('\n\nError: Terminator "@" Missing at End of Line')
                    sys.exit()
                else:
                    return (' = ',val, exp)
        else:
            print('Error after',
                self.tok.type ,': Expected an OPERATOR, but got',
                self.nexttok.type)
            sys.exit()
    def expr(self):
        'EXP -> EXP PLUS TERM | EXP MINUS TERM | TERM'
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = (' + ', exprval, right)
            elif op == 'MINUS':
                exprval = (' - ', exprval, right)
        if self.nexttok.value!='@':
            print('\n\nError: Terminator "@" Missing at End of Line')
            sys.exit()
        else:
            return exprval
    def term(self):
        'TERM -> TERM TIMES FACTOR | TERM DIVIDE FACTOR | FACTOR'
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = (' * ', termval, right)
            elif op == 'DIVIDE':
                termval = (' / ', termval, right)
                    
        return termval
    def factor(self):
        'FACTOR -> EXP | INT | ID'
        if self._accept('INT') and not (self.nexttok.type == 'INT' or self.nexttok.type == 'ID'):
            return int(self.tok.value)
        elif self._accept('ID') and not (self.nexttok.type == 'INT' or self.nexttok.type == 'ID'):
            return self.tok.value
        elif (self.tok.type == 'INT' or self.tok.type == 'ID') and (self.nexttok.type == 'INT' or self.nexttok.type == 'ID'):
            print('Error after',
                self.tok.type ,': Expected an OPERATOR, but got',
                self.nexttok.type)
            sys.exit()
        else:
            print('Error after',
                self.tok.type ,': Expected an INT or ID, but got',
                self.nexttok.type)
            sys.exit()


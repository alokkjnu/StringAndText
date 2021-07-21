# Writing a Simple Recursive Decent Parser

from os import terminal_size
import re
import collections
from sre_constants import RANGE_UNI_IGNORE, SRE_FLAG_LOCALE
# Token Specification

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

#Tokenizer

Token = collections.namedtuple('Token',['type','value'])
def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

#Parser
class ExpressionEvaluator:
    '''
    Implementation of a recursive decent parser. Each method implements a single grammer rule.
     Use the ._accept() method to test and accept the current lookahead token. Use the ._except()
     method to exactly match and discard the next token on on the input 
     (or raise a SyntaxError if it doesn't match).
    '''

    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self,toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
    
    def _except(self,toktype):
        'Cosnsume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammer rules follow

    def expr(self):
        "expression ::= term { ('+'|'-')term}*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/')factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | (expr)"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._accept('RPAREN')
            return exprval
        else:
            raise SyntaxError("Expected Number or LPAREN")

e = ExpressionEvaluator()
c = e.parse('2')    
print(c)
d = e.parse('2 + 3')
print(d)
f = e.parse('2 + 3 * 4')
print(f)
g = e.parse('2 + ( 3 + 4 ) * 5')
print(g)

class ExpressionTreeBulder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term{( '+'|'-) term}'"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+',exprval, right)
            elif op == 'MINUS':
                exprval = ('-',exprval,right)
        return exprval
    def term(self):
        "term ::= factor { ( '*' | '/') factor }"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*',termval,right)
            elif op == 'DIVIDE':
                termval = ('/',termval,right)
        return termval
    
    def factor(self):
        'factor ::= NUM | ( expr )'
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._accept('RPAREN')
            return exprval
        else:
            raise SyntaxError("Expected NUM or LPAREN")

e = ExpressionTreeBulder()
i = e.parse(' 2 + 3')
print(i)
j = e.parse('2 + 3 * 4')
print(j)
k = e.parse('2 + (3 + 4) *5')
print(k)
l = e.parse('2 + 3 + 4')
print(l)
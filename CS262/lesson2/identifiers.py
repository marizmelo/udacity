import ply.lex as lex # import lex analyzer lib

tokens = (
  'IDENTIFIER', # valid identifiers 
  )

t_ignore = ' ' # shortcut for whitespace

def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)


def t_IDENTIFIER(token):
  r'^[a-z A-Z][a-z A-Z_0-9.]*'
  return token

identifier = "factorial"  # invalid: _factorial , 123factorial

identifierlex = lex.lex()
identifierlex.input(identifier)


while True:
  tok = identifierlex.token() # return next token available
  if not tok: break
  print tok
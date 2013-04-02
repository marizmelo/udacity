import ply.lex as lex # import lex analyzer lib

tokens = (
  'NUMBER', # valid numbers 
  )

t_ignore = ' ' # shortcut for whitespace

def t_error(token):
    print("Illegal number '%s'" % token.value[0])
    token.lexer.skip(1)


def t_NUMBER(token):
  r'-?[0-9]+(:?\.[0-9]*)?'
  token.value = float(token.value)
  return token

numbers = "-4.6"  # invalid: 3.4.5.5 a23

identifierlex = lex.lex()
identifierlex.input(numbers)


while True:
  tok = identifierlex.token() # return next token available
  if not tok: break
  print tok
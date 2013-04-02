import ply.lex as lex # import lex analyzer lib

tokens = (
  'IDENTIFIER', # valid numbers 
  'WORD',
  )

t_ignore = ' ' # shortcut for whitespace

def t_error(token):
    print("Illegal comment '%s'" % token.value[0])
    token.lexer.skip(1)


def t_COLCOMMENT(token):
  r'//[^\n]*'
  pass

def t_IDENTIFIER(token):
  r'^[a-z A-Z][a-z A-Z_0-9.]*'
  return token


sentence = "hello // comment here" 

jscommentlexer = lex.lex()
jscommentlexer.input(sentence)


while True:
  tok = jscommentlexer.token() # return next token available
  if not tok: break
  print tok
import ply.lex as lex # import lex analyzer lib

tokens = (
  'NEWLINE', # \n
  'LANGLE', # <
  'LANGLESLASH', # </
  'RANGLE', # >
  'EQUAL', # = 
  'NUMBER', # 33
  'STRING', # "hello"
  'WORD', # Welcome!
  )

# lexer states
states = (
  ('htmlcomment', 'exclusive'), # if you are in the middle of process HTML comment don't do anything else
)

t_htmlcomment_ignore = '//[^\n]'

t_ignore = ' ' # shortcut for whitespace

def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)

# Specifying Tokens

# detecting HTML comments
def t_htmlcomment(token):
  r'<!--'
  token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
  r'-->'
  token.lexer.lineno += token.value.count("\n") 
  token.lexer.begin('INITIAL') # INITIAL mode is whenever the lexer was doing before enter on comment mode

def t_htmlcomment_error(token):
  token.lexer.skip(1) # like pass

# new lines
def t_newline(token):
  r'\n'
  token.lexer.lineno += 1 # lineno is a variable of LEXER that counts number of lines
  pass

# Write code for the LANGLESLASH to match </ in our HTML.
def t_LANGLE(token):
  r'<'
  return token

def t_LANGLESLASH(token):
  r'</'
  return token

def t_RANGLE(token):
  r'>'
  return token

def t_EQUAL(token):
  r'='
  return token

# match numbers strings and convert them to int
def t_NUMBER(token):
  r"[0-9]+"
  token.value = int(token.value)
  return token

# match double quoted string without a " inside
def t_STRING(token):
  r'"[^"]*"'
  token.value = token.value[1:-1] # substring to strip double quotes
  return token  

# WORD is any number of chars EXCEPT <> or space
def t_WORD(token):
  r"[^ <>\n]+"
  return token

#webpage = '"This" is 33 <b>my</b> webpage!'
# webpage = """Line1
#   Line2
# """
webpage = """hello <!-- comment --> all"""

htmllexer = lex.lex() # tells lex to use all token def above
htmllexer.input(webpage) # which string to break up

while True:
  tok = htmllexer.token() # return next token available
  if not tok: break
  print tok

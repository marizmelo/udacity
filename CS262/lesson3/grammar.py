# Grammar with 4 rewrite rules
grammar = [
  ("exp", ["exp", "+", "exp"]),
  ("exp", ["exp", "-", "exp"]),
  ("exp", ["(", "exp", ")"]),
  ("exp", ["num"]),
]

def expand(tokens, grammar):
  for pos in range(len(tokens)):
    for rule in grammar:
      if tokens[pos] == rule[0]:
        yield tokens[0:pos] + rule[1] + tokens[pos + 1:]

depth = 1

utterances = [["exp"]]

# for x in range(depth):
#     for sentence in utterances:
#         utterances = utterances + [ i for i in expand(sentence, grammar)]

# for sentence in utterances:
#     print sentence


print utterances + [i for i in expand(["exp"], grammar)]


# "a exp"
# expanded to depth 1 
# "a exp + exp"
# "a exp - exp"
# "a (exp)"
# "a num"  
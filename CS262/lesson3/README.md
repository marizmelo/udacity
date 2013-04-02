Lesson 3 Notes
==============

**Noan Chomsky** 1955
- utterances have rules (syntatic structures) (formal grammars)

grammatical sentences

formal grammars

non-terminals vs terminals

non-terminals can be replaced
terminals can't

derivation - the process to create meaningful sentences

possible utterances

ex:

    sentence -> subj + verb

    subj -> students
    subj -> teachers
    subj -> subj and subj  // compound rule

    verb -> think
    verb -> write

new derivation using the rules above

    students and teachers think

this process is called **recursive rewrite rule** in the grammar

Arithmetic expression

    exp -> exp + exp
    exp -> exp - exp
    exp -> number (terminal)

derivations

    number
    number + number + number
    number - number + number

inverted tree format (parse tree)

            exp
          /  |  \
        exp  +  exp
       / | \     |
     exp + exp  num
      |     |
     num   num


RECALL

**Lexical Analysis (lexing)**
  process of breaking string into list of tokens (words)

**Syntactical Analysis (parsing)**
  take list of words (tokens) check if follows grammar


Lexing (word rules)
Parsing (sentence rules)

Putting them together = expressive power (creativity)

    stmt -> identifier = exp
    exp -> exp + exp
    exp -> exp - exp
    exp -> number

Grammars can encode **Regular Languages**

Grammars >= (strict greater than) Regexp

Anything we can specify in Regexp can be specified with Grammars

ex.:

    regexp = r'p+i?'

    regexp -> pplus iopt
    pplus -> p pplus  (recursive rewrite rule)
    pplus -> p
    iopt -> i
    iopt -> e

    // pi pi ppi etc...


Regular expressions describe **regular languages**

Grammar describe **context free languages**

regexp != context free grammars

curiosity: balanced parentheses were extensively studied by Walther von Dyck (a German mathematician)

Balanced parenthesis are not regular (regexp)
Is impossible to express balanced parenthesis in regex

A grammar is **ambiguous** if **at least 1** string in the grammar has **more than 1** different parse tree

tree can be right or left heavy depending of length of side. More nodes on the left or more nodes on the right. 

**Turing complete languages**

syntactical evaluation

Creating Grammars vs checking Utterances

LAMBDA = make me a function

mapReduce function

    map( mysquare, [1, 2, 3, 4, 5])


**Brendan Eich** CTO Mozilla and creator of JavaScript explains anonymous functions in javaScript as a implementation of lambdas expressions

list comprehension in python


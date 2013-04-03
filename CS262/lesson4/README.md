Lesson 4 Notes
==============

Memoization is a computer science technique in which we keep a "chart" or "record" of previous computations and compute new values in terms of previous answers.

Ambiguity in JS

Brute force algorithm from last lesson (try all the options exhaustively)

Brute force means to try all options exhaustively. Easy to code but relatively inefficient.

Parsing idea
1. being lazy
2. don't duplicate work (DRY)

Larry wall - designer and inventor of Perl. The three greatest virtues of a computer programmer: 
1. Laziness
2. Impatience
3. Hubris

Fibonacci as a way to teach recursion

    def fibo(n):
      if n <= 2:
        return 1
      else:
        return fibo(n - 1) + fibo(n - 2)

Super slow implementation of Fibonacci function (brute force)

Increasing the number by 1 is duplicating the time need to calculate the sequence


Parsing state is a rewrite rule from the grammar augmented with 1 point on the right-hand side or the rule.


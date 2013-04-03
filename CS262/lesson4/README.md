Lesson 4 Notes
==============

Memoization - from Wikipedia: technique used primarily to speed up computer programs by having function calls avoid repeating the calculation of results for previously processed inputs.

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
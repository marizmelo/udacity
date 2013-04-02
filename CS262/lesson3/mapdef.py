def mysquare(x): return x * x

print map( mysquare, [1, 2, 3, 4, 5])

print map( lambda(x): x * x, [1, 2, 3, 4, 5]) # this use of lambda is sometimes called anonymous function

print [len(x) for x in ["hello", "my", "friends"]]

print [x * x for x in [1, 2, 3, 4, 5]]
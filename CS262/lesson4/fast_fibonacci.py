# Fibonacci Memoization
chart = {}
def memoFibo(n):
  if n in chart:
    return chart[n] # lazy
  elif n <= 2:
    chart[n] = 1
  else:
    chart[n] = memoFibo(n-1) + memoFibo(n-2)
  return chart[n]

print memoFibo(30)
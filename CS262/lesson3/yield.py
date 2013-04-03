# functions that use yield are called generator functions
def odd_numbers(numbers):
  for n in numbers:
    if n % 2 == 1:
      yield n

print [x for x in odd_numbers([1, 2, 3, 4, 5])]


# list comprehension
print [x for x in [1, 2, 3, 4, 5] if x % 2]

# compound expression
print [x * 2 for x in [1, 2, 3, 4, 5] if x % 2]
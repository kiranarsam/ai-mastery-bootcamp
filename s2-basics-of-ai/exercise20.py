#
# List comprehensive

# [expression for item in iterable if condition]

# create  a list of squares
squares = [ x**2 for x in range(10) if x % 2 == 0 ]

print(squares)

evens = [ x for x in range(10) if x % 2 == 0 ]
print(evens)

## Lambda functions
# Syntax: lambda arguments: expression
add = lambda x,y : x + y
print(add(3, 3))


## map()
numbers = [1,2,3,4]

squares = map(lambda x: x**2, numbers)
print(squares)
print(list(squares))

# filter()
evenList = filter(lambda x: x % 2 == 0, numbers)

print(evenList)
print(list(evenList))

# reduce()
from functools import reduce
product = reduce(lambda x,y: x * y, numbers)

print(product)

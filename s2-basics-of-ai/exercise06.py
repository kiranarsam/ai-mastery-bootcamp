# functions

def function_name(parameters):
  # Code block
  pass


# function with parameters and return values
def add_numbers(a, b):
  return a + b

result = add_numbers(10, 20)
print("Sum: ", result)

# Scope and Lifetime of the program
# local scope
# global scope
# lifetime


def greet():
  message = "Hello World"
  print(message)

greet()
#print(message) # error

greeting = "hi"

def say_hello():
  print(greeting + " from inside the say_hello() ")

say_hello()
print(greeting + " from outside the say_hello()")

# importing modules
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m   # alias
print(m.sqrt(16))
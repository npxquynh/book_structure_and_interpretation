# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

import math

even = lambda x : (x % 2) == 0
square = lambda x : x * x
halve = lambda x : math.floor(x / 2)

def fast_exp_loop(base, exponential):
  """Returns the exponential of base ^ exponential

  Complexity: log(n)
  """
  result = 1
  z = base

  while (exponential != 0):
    if not even(exponential):
      result *= z

    z = square(z)
    exponential = halve(exponential)

  return result

def fast_exp_recursion(base, exponential):
  """Returns the exponential of base ^ exponential

  Complexity: log(n)
  """
  if exponential == 1:
    return base
  elif even(exponential):
    return square(fast_exp_recursion(base, halve(exponential)))
  else:
    return base * square(fast_exp_recursion(base, halve(exponential)))


print(fast_exp_loop(2, 23))
print(fast_exp_recursion(2, 23))

print(math.pow(2, 23))

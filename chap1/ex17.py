# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

import math

double = lambda x : x * 2
halve = lambda x : math.floor(x / 2)
even = lambda x : x % 2 == 0

def fast_mult_loop(x, n):
  """Returns the multiplication of x * n using only addition (+) operation, halve, and double

  Complexity: log(n)
  """
  result = 0
  z = x

  while (n != 0):
    if not even(n):
      result += z

    z = double(z)
    n = halve(n)

  return result


def fast_mult_recursion(x, n):
  """
  Returns the multiplication of x * n using only addition (+) operation, halve, and double

  Complexity: log(n)
  """
  if n == 1:
    return x
  elif even(n):
    return double(fast_mult_recursion(x, halve(n)))
  else:
    return x + double(fast_mult_recursion(x, halve(n)))

print(fast_mult_loop(143, 37))
print(fast_mult_recursion(143, 37))

print(143 * 37)

# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 1.39: Approximate tan(x)

import math

def tan_continued_fraction(x, k):
  """Computes tan(x)
  """
  def n(i):
    if i == 1:
      return x
    else:
      return x * x

  def d(i):
    return (i - 1) * 2 + 1

  result = n(k) / d(k)
  i = k - 1
  while (i > 0):
    result = n(i) / (d(i) - result)
    i -= 1

  return result

print(tan_continued_fraction(3, 10))
print(math.tan(3))

import math

def iterative_multiplication(x, n):
  """Returns the multiplication of x * n using only addition (+) operation
  Complexity: log(n)
  """
  result = 0
  z = x

  while (n != 0):
    if n % 2 == 1:
      result += z

    z = z + z
    n = math.floor(n / 2)

  return result

print(iterative_multiplication(143, 37))

print(143 * 37)

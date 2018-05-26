import math

def iterative_exponential(x, n):
  """Returns the exponential of x^n
  Complexity: log(n)
  """
  result = 1
  z = x

  while (n != 0):
    if n % 2 == 1:
      result *= z

    z = z * z
    n = math.floor(n / 2)

  return result

print(iterative_exponential(2, 23))

print(math.pow(2, 23))

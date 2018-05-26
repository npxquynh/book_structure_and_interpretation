import math

def fibonacci(n):
  return iterative_fibonacci(0, 1, 0, 1, n)

def iterative_fibonacci(a, b, p, q, count):
  """Returns the fibonacci(count) using the exponential squaring with identity matrix
    A = [p q  ]
        [q p+q]

  => A^2 = [p' q'     ]
           [q' p' + q']

  ==> p' = p*p + q*q
  ==> q' => p*q + q*p + q*q

  (a, b) = (0, 1)
  a = Fibonacci(count)
  b = Fibonacci(count + 1)

  A * (a, b) = [p q  ] (a) = (p*a + q*b)
               [q p+q] (b)   (q*a + p*b + q*b)

  Complexity: log(n)
  """

  print(count, ' : ', a, "--", b, '   ', p, '--', q)
  if count == 0:
    return b
  elif count % 2 == 0:
    return iterative_fibonacci(a, b, p*p + q*q, q*q + 2*p*q, math.floor(count/2))
  else:
    return iterative_fibonacci(p*a + q*b, q*a + p*b + q*b, p, q, count - 1)

for i in range(0, 10):
  print(fibonacci(i), "\n")

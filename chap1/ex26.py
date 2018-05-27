# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Report runtime for searching for prime numbers with Fermat test, and 'x * x' operator instead of calling square(x) in expmod()

import time
import math
import random

def remainder(x, y):
  return x % y

def square(x):
  return x * x

def halve(x):
  return math.floor(x / 2)

def expmod(base, exp, m):
  """Computes the exponential of a number modulo another number
  (base ^ exp) % m
  Aka: implementation for function pow(base, exp, m)
  """
  if exp == 0:
    return 1
  elif exp % 2 == 0:
    return remainder(
      # When we call expmod() twice, the expansion grow exponentially, and it causes problem.
      (expmod(base, halve(exp), m)) * (expmod(base, halve(exp), m)),
      m
    )
  else:
    return remainder(base * expmod(base, exp - 1, m), m)

def fermat_test(n):
  """Returns true if n pass Fermat test
  if n is a prime number, then we can pick a random a such that 0 < a < n, and we have (a^n) % n == a
  """
  a = random.randint(0, n)
  return expmod(a, n, n) == a

def fast_prime(n, times):
  i = 0

  while (i < times):
    if not fermat_test(n):
      break
    i += 1

  if i == times:
    return True
  else:
    return False

def is_prime(n):
  times = 10
  return fast_prime(n, 10)

def timed_prime_test(n):
  return start_prime_test(n, time.time())

def start_prime_test(n, start_time):
  if is_prime(n):
    report_prime(n, time.time() - start_time)
    return True
  else:
    return False

def report_prime(n, elapsed_time):
  print('***')
  print("%i\t%.1E" % (n, elapsed_time))

def search_for_prime_recursive(from_n, count):
  """Check for primality of consecutive odd integers in a specified range
  """
  from_n = from_n + 1 if from_n % 2 == 0 else from_n
  if count == 0:
    print('..')
  elif timed_prime_test(from_n):
    search_for_prime_recursive(from_n + 2, count - 1)
  else:
    search_for_prime_recursive(from_n + 2, count)

search_for_prime_recursive(1000, 3)
search_for_prime_recursive(10000, 3)
search_for_prime_recursive(100000, 3)
search_for_prime_recursive(1000000, 3)

# Result
# Running is significantly slower with 'x * x'.
# ***
# 1009  6.1E-03
# ***
# 1013  7.6E-03
# ***
# 1019  7.6E-03
# ..
# ***
# 10007 8.5E-02
# ***
# 10009 8.6E-02
# ***
# 10037 9.0E-02
# ..
# ***
# 100003  7.9E-01
# ***
# 100019  7.8E-01
# ***
# 100043  7.7E-01
# ..
# ***
# 1000003 6.9E+00
# ***
# 1000033 6.8E+00
# ***
# 1000037 6.9E+00

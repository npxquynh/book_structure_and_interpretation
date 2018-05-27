# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Report runtime for searching for prime numbers with Fermat test and fast_exp

import time
import math
import random

def remainder(x, y):
  return x % y

def square(x):
  return x * x

def halve(x):
  return math.floor(x / 2)

def fast_exp(base, exp):
  if exp == 0:
    return 1
  elif exp % 2 == 0:
    return square(fast_exp(base, halve(exp)))
  else:
    return base * square(fast_exp(base, halve(exp)))

def expmod(base, exp, m):
  """Computes the exponential of a number modulo another number
  (base ^ exp) % m
  Aka: implementation for function pow(base, exp, m)
  """
  return remainder(fast_exp(base, exp), m)

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
# The running time increases significantly
# Because with this one, the resulting number of exponential will be really huge and it increases the overall
# processing time

# ***
# 1009  2.6E-04
# ***
# 1013  3.4E-04
# ***
# 1019  3.6E-04
# ..
# ***
# 10007 1.2E-02
# ***
# 10009 1.7E-02
# ***
# 10037 1.3E-02
# ..
# ***
# 100003  6.6E-01
# ***
# 100019  7.3E-01
# ***
# 100043  7.4E-01
# ..

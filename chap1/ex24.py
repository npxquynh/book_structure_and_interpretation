# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Report runtime for searching for prime numbers with Fermat test

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
    return remainder(square(expmod(base, halve(exp), m)), m)
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
# Increasing the result search from 10^5 to 10^6 doesn't increase the time
# ***
# 1009  7.6E-05
# ***
# 1013  1.1E-04
# ***
# 1019  1.1E-04
# ..
# ***
# 10007 1.3E-04
# ***
# 10009 1.1E-04
# ***
# 10037 9.8E-05
# ..
# ***
# 100003  1.5E-04
# ***
# 100019  2.1E-04
# ***
# 100043  1.9E-04
# ..
# ***
# 1000003 2.1E-04
# ***
# 1000033 1.7E-04
# ***
# 1000037 1.7E-04

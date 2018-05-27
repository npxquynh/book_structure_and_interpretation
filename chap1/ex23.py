# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Report runtime for searching for prime numbers with smallest divisor, searching for only odd numbers

import time
import math
import random

def remainder(x, y):
  return x % y

def square(x):
  return x * x

def next(x):
  if x == 2:
    return 3
  else:
    return 2

def smallest_divisor(n):
  i = 3
  while (square(i) <= n):
    if remainder(n, i) == 0:
      return i
    i += next(i)
  return n

def is_prime(n):
  return smallest_divisor(n) == n

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

def search_for_prime_loop(from_n, count):
  found_prime_numbers = []
  from_n = from_n + 1 if from_n % 2 == 0 else from_n
  while(len(found_prime_numbers) < count):
    if timed_prime_test(from_n):
      found_prime_numbers.append(from_n)

    from_n += 2

# search_for_prime_loop(1000, 3)
# search_for_prime_loop(2000, 3)

search_for_prime_recursive(1000, 3)
search_for_prime_recursive(10000, 3)
search_for_prime_recursive(100000, 3)
search_for_prime_recursive(1000000, 3)

# Result
# The new running time with modified smallest_divisor is faster than the one in ex22
# ***
# 1009  5.2E-06
# ***
# 1013  5.0E-06
# ***
# 1019  5.0E-06
# ..
# ***
# 10007 1.5E-05
# ***
# 10009 1.5E-05
# ***
# 10037 1.4E-05
# ..
# ***
# 100003  7.5E-05
# ***
# 100019  6.9E-05
# ***
# 100043  6.9E-05
# ..
# ***
# 1000003 2.3E-04
# ***
# 1000033 2.6E-04
# ***
# 1000037 1.7E-04

# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Report runtime for searching for prime numbers

import time
import math
import random

def remainder(x, y):
  return x % y

def square(x):
  return x * x

def smallest_divisor(n):
  i = 2
  while (square(i) <= n):
    if remainder(n, i) == 0:
      return i
    i += 1
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

# ***
# 1009  6.9E-06
# ***
# 1013  8.1E-06
# ***
# 1019  6.9E-06
# ..
# ***
# 10007 2.2E-05
# ***
# 10009 4.2E-05
# ***
# 10037 5.1E-05
# ..
# ***
# 100003  1.6E-04
# ***
# 100019  1.3E-04
# ***
# 100043  1.4E-04
# ..
# ***
# 1000003 3.9E-04
# ***
# 1000033 3.3E-04
# ***
# 1000037 2.7E-04

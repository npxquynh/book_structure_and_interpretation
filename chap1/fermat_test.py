# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 2 - Procedures and the Processes They Generate

# Fermat's Little Theorem

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


times = 20

for i in range(1, 100):
  n = random.randint(1, 5000)
  if fast_prime(n, times):
    print('---', n)

print("Fermat test should not output these Carmichael numbers:")
carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601]
for n in carmichael_numbers:
  if fast_prime(n, times):
    print('---', n)

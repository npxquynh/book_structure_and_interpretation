# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 1.36: print the sequence of approximations, with and without average damping
# With average damping, the sequence of approximation is shorter. It means that we can find result faster.

import math

def fixed_point(f, first_guess, tolerance = 0.0001):
  def close_enough(x, y):
    return abs(x - y) < tolerance

  def try_guess(guess):
    print('%.4f' % guess)
    next_guess = f(guess)

    if close_enough(guess, next_guess):
      return next_guess
    else:
      return try_guess(next_guess)

  return try_guess(first_guess)

def find_solution():
  f = lambda x : math.log(1000) / math.log(x)
  return fixed_point(f, 1.1)

def find_solution_with_average_damping():
  f = lambda x : (x + math.log(1000) / math.log(x)) / 2
  return fixed_point(f, 1.1)

print(find_solution())
print('***')
print(find_solution_with_average_damping())

# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.46: General computational strategy "iterative improvement"

def iterative_improve(close_enough, improve_guess):
  def execute(guess):
    next_guess = improve_guess(guess)
    print(guess)
    if close_enough(guess, improve_guess(guess)):
      return guess
    else:
      return execute(next_guess)

  return execute

def fixed_point(f, first_guess, tolerance = 0.0001):
  def close_enough(x, y):
    return abs(x - y) < tolerance

  def improve_guess(guess):
    return ((guess + f(guess)) / 2)

  return iterative_improve(close_enough, improve_guess)(first_guess)

def sqrt(x):
  def f(y):
    return x / y

  return fixed_point(f, 2)

print(sqrt(9))

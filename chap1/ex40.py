# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.40: Approximate resule of cubic function with Newton's method

dx = 0.00001

def fixed_point(f, first_guess, tolerance = 0.0001):
  def close_enough(x, y):
    return abs(x - y) < tolerance

  def try_guess(guess):
    next_guess = f(guess)
    if close_enough(guess, next_guess):
      return next_guess
    else:
      return try_guess(next_guess)

  return try_guess(first_guess)


def derivative(g):
  def tmp(x):
    return (g(x + dx) - g(x)) / dx

  return tmp


def newton_transform(g):
  def tmp(x):
    return x - (g(x) / derivative(g)(x))

  return tmp


def newtons_method(f, guess):
  return fixed_point(newton_transform(f), guess)


cube = lambda x : x * x * x
print(derivative(cube)(3))
print(newtons_method(cube, 1))

def cubic(a, b, c):
  def tmp(x):
    return x * x * x + a * x * x + b * x + c

  return tmp

print("\nWe have 3 solutions for x^3 - 7x^2 + 4x + 12, depending on the first guess value:")
print(newtons_method(cubic(-7, 4, 12), -3))
print(newtons_method(cubic(-7, 4, 12), 1))
print(newtons_method(cubic(-7, 4, 12), 5))

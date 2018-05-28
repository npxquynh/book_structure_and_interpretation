# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 35: Compute the golden ratio by a 'fixed_point' function

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

golden_ratio = lambda x : 1 + 1 / x

print(fixed_point(golden_ratio, 1))

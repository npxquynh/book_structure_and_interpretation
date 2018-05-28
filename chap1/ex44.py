# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.44" Define the 'smooth' procedures
# And then define 'n-fold smoothed function'

def compose(f, g):
  def result(x):
    return f(g(x))

  return result

def repeated_recursive(f, times):
  def get_result(f, count):
    if count == 1:
      return f
    else:
      return compose(f, get_result(f, count - 1))

  return get_result(f, times)

dx = 0.00001

def smooth(f):
  smoothed = lambda x : (f(x - dx) + f(x) + f(x + dx)) / 3

  return smoothed

def n_fold_smooth_function(f, n):
  return repeated_recursive(smooth(f), n)

square = lambda x : x * x
print(smooth(square)(3))
print(n_fold_smooth_function(square, 1)(3))
print(n_fold_smooth_function(square, 2)(3))
print(n_fold_smooth_function(square, 3)(3))

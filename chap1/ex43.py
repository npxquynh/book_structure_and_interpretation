# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.43: Define the 'repeated' procedures to apply original procedures multiple time

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

def repeated_loop(f, times):
  def get_result(x):
    result = f(x)
    i = 1
    while (i < times):
      result = f(result)
      i += 1
    return result

  return get_result

square = lambda x : x * x
triple = lambda x : 3 * x

print(repeated_loop(triple, 3)(3))
print(repeated_recursive(triple, 3)(3))

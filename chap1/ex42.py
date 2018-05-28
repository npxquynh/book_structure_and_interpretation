# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.42: Define the 'compose' procedures

def compose(f, g):
  def result(x):
    return f(g(x))

  return result

square = lambda x : x * x
increase = lambda x : x + 1

print(compose(square, increase)(2))

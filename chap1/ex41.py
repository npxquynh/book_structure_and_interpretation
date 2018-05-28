# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 4 - Procedures as Returned Values

# Exercise 1.41: Define the 'double' procedures to apply original procedures twice

def double():
  def d1(f):
    def d2(x):
      return f(f(x))

    return d2

  return d1

increase = lambda x : x + 1

print(double()(increase)(2))

print(double()(double()(increase))(2))

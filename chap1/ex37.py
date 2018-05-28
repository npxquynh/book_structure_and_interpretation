# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 1.37: Implement continued fraction

def cont_frac_linear_recursive(n, d, k):
  def next_result(index):
    if index == k:
      return n(k) / d(k)
    else:
      return n(index) / (d(index) + next_result(index + 1))

  return next_result(1)

def cont_frac_iterative_recursive(n, d, k):
  result = n(k) / d(k)
  i = k - 1
  while (i > 0):
    result = n(i) / (d(i) + result)
    i -= 1

  return result

n = lambda i : 1.0
d = lambda i : 1.0
print(cont_frac_linear_recursive(n, d, 100))
print(cont_frac_iterative_recursive(n, d, 100))
print(cont_frac_iterative_recursive(n, d, 0))
print(cont_frac_iterative_recursive(n, d, 1))

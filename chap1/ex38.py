# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 1.39: Approximate the base of natural logarithms

def cont_frac_linear_recursive(n, d, k):
  def next_result(index):
    if index == k:
      return n(k) / d(k)
    else:
      return n(index) / (d(index) + next_result(index + 1))

  return next_result(1)

def n(i):
  return 1.0

def d(i):
  if i <= 2:
    return i
  elif (i - 2) % 3 == 0:
    return ((i - 2) / 3) * 2
  else:
    return 1

print("Approximate e")
print(2 + cont_frac_linear_recursive(n, d, 100))

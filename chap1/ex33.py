# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 33: Write 'filtered_accumulate' that combines only those terms derived from values in the
# range that satisfy a specified condition

def filtered_accumulale(combiner, null_value, term, after, filtered, a, b):
  if a > b:
    return null_value
  elif filtered(a):
    return combiner(term(a), filtered_accumulale(combiner, null_value, term, after, filtered, after(a), b))
  else:
    return filtered_accumulale(combiner, null_value, term, after, filtered, after(a), b)

add_combiner = lambda x, y : x + y
ten_fold = lambda x : x * 10
increase = lambda x : x + 1
is_even = lambda x : x % 2 == 0

print(filtered_accumulale(add_combiner, 0, ten_fold, increase, is_even, 1, 10))

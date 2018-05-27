# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 30: translate sum(term, a, next, b) into an iterative recursion

def sum_linear_recursion(term, a, after, b)
  # term: square(x)
  # a: 0
  # after: increase(x)
  # b: 3

  if (a > b)
    0
  else
    term.call(a) + sum_linear_recursion(term, after.call(a), after, b)
  end
end

def sum_iterative_recursion(term, a, after, b)
  iter = lambda do |a, result|
    if a > b
      result
    else
      iter.call(after.call(a), term.call(a) + result)
    end
  end

  iter.call(a, 0)
end

square = lambda { |x| x * x }
increase = lambda { |x| x + 1 }
puts sum_linear_recursion(square, 1, increase, 3)
puts sum_iterative_recursion(square, 1, increase, 3)

# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 31: Write a higher order procedures that returns the product of the values of a function a points over a given range.

def product_linear_recursion(term, a, after, b)
  if (a > b)
    1
  else
    term.call(a) * product_linear_recursion(term, after.call(a), after, b)
  end
end

def product_iterative_recursion(term, a, after, b)
  iter = lambda do |a, result|
    if a > b
      result
    else
      iter.call(after.call(a), result * term.call(a))
    end
  end

  iter.call(a, 1)
end

pi_factor = lambda { |x| x * (x + 2.0) / (x + 1) / (x + 1) }
increase = lambda { |x| x + 2 }

puts product_linear_recursion(pi_factor, 2, increase, 200) * 4
puts product_iterative_recursion(pi_factor, 2, increase, 200) * 4


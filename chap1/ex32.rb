# Structure and Interpretation of Computer Programs
# Chapter 1 Building Abstractions with Procedures
# Section 3 - Formulating Abstractions with Higher-Order Procedures

# Exercise 32: Write 'accumulate' that combines a collection of terms, using some genral accumulation function

def accumulate_linear_recursion(combiner, null_value, term, a, after, b)
  if a > b
    null_value
  else
    combiner.call(term.call(a), accumulate_linear_recursion(combiner, null_value, term, after.call(a), after, b))
  end
end

def accumulate_loop(combiner, null_value, term, a, after, b)
  result = null_value

  while (a < b)
    result = combiner.call(result, term.call(a))
    a = after.call(a)
  end

  result
end

def accumulate_iterative_recursion(combiner, null_value, term, a, after, b)
  iter = lambda do |a, result|
    if a > b
      result
    else
      iter.call(after.call(a), combiner.call(result, term.call(a)))
    end
  end

  iter.call(a, null_value)
end

product = lambda { |x, y| x * y }
add = lambda { |x, y| x + y }

pi_factor = lambda { |x| x * (x + 2.0) / (x + 1) / (x + 1) }
increase = lambda { |x| x + 2 }

puts accumulate_linear_recursion(product, 1, pi_factor, 2, increase, 200) * 4
puts accumulate_loop(product, 1, pi_factor, 2, increase, 200) * 4
puts accumulate_iterative_recursion(product, 1, pi_factor, 2, increase, 200) * 4


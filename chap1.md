# Chapter 1: Building Abstractions with Procedure

## 1.1 The Elements of Programming

```
(define (square x)
  (* x x))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))
```

**Normal-order evaluation**
- It would substitute operand expressions for parameters until it obtained an expressions involving only primitive operators, and would then perform the evaluation.

- "fully expand and then reduce"


```
# Fully expand

(f 5)
(sum-of-squares (+ 5 1) (* 5 2))
(+     (square (+ 5 1))      (square (* 5 2)        )
(+     (* (+ 5 1) (+ 5 1))   (* (* 5 2) (* 5 2))    )

# And then reduce

(+     (* 6 6)               (* 10 10)              )
(+     36                    100                    )
136
```

**Applicative-order evaluation**

"Evaluate the arguments and then apply"

1. Evaluate the operators to get the precedure to be applied
2. Evaluate the operands to get the arguments
3. Apply the procedure to the arguments

```
(f 5)

# Evaluate f by retrieve the body of f
(sum-of-squares (+ a 1) (* a 2))

# Replace the formal parameter 'a' by the argument 5
(sum-of-squares (+ 5 1) (* 5 2))

# Evaluate the operator sum-of-squares by retrieving the body of sum-of-squares
(+ (square x) (square y))

# Evaluate the operands
(+ 5 1) produces 6
(* 5 2) produces 10

# Apply the sum-of-squares procedures to 6 and 10
(+ (square 6) (square 10))

# Then we apply the 'square' procedure
(+ (* 6 6) (* 10 10))

# Reduce
(+ 36 100)
136
```

**Exercise 16, 17: evaluation of powers**

More detail can be found in Knuth (1981), section 4.6.3

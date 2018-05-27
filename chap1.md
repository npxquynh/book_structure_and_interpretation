# Chapter 1: Building Abstractions with Procedure

## 1.1 The Elements of Programming

###
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

## 1.2 Procedures and the Processes they Generate

### 1.2.1 Linear Recursion and Iteration

**Recursive process**

_recursive process_ following the substitution model, as the process builds up a chain of _deferred operations_, the interpreter must keep track of the operations to be performed later on.

_linear recusive process_ the process with the length of a chain _deferred operations_ grow linearly. Example:

```
def sum(n):
  if n == 0:
    return 0
  else:
    return 1 + sum(n-1)
```

_iterative recusrive process_ the process that does not grow and shrink as it builds up a chain of _deferred operations_. Example:

```
def sum(n, result):
  if n == 0:
    return result
  else:
    return sum(n - 1, result + 1)
```

_recursive procedure_ translates into having its definition refers to itself

**Exercise 16, 17: evaluation of powers**

More detail can be found in Knuth (1981), section 4.6.3

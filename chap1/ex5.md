# Structure and Interpretation of Computer Programs
# Chapter 1 Section 1 Elements of Programming

We have the following two procedures:

```
(define (p) (p))

(define (test x y)
  (if (= x 0)
    0
    y))
```

## When using normal-order evaluation

```
# Expand fully

(test 0 (p))

(if (= 0 0)
    0
    (p))

# Expand if. Because the predicate is true, it evalutes the consequent, which is

0

```

## When using applicative-order evaluation

```

(test 0 (p))

# Evaluate the operands

0 --> 0

(p) --> (p) --> (p) --> it keeps on expanding (p) forever

```

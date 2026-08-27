# ============================================================
#                    PYTHON GENERATORS
# ============================================================

# ------------------------------------------------------------
# 1. WHAT IS A GENERATOR?
# ------------------------------------------------------------

# Definition:
# A generator is a special type of function that produces
# values one at a time instead of returning all values at once.
#
# Generators use the 'yield' keyword.
#
# Advantages:
# 1. Saves memory
# 2. Produces values one at a time
# 3. Supports lazy evaluation
# 4. Useful for large or infinite sequences


# ------------------------------------------------------------
# 2. NORMAL FUNCTION vs GENERATOR FUNCTION
# ------------------------------------------------------------

# Normal function
def normal_function():
    return [1, 2, 3, 4, 5]


result = normal_function()
print(result)


# Generator function
def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


g = generator_function()

print(next(g))
print(next(g))
print(next(g))


# ------------------------------------------------------------
# 3. yield KEYWORD
# ------------------------------------------------------------

# Definition:
# 'yield' is used inside a generator function.
# It produces a value and pauses the execution of the function.
#
# When next() is called again, the function continues
# from where it was paused.

def numbers():
    yield 10
    yield 20
    yield 30


g = numbers()

print(next(g))       # 10
print(next(g))       # 20
print(next(g))       # 30


# ------------------------------------------------------------
# 4. next() FUNCTION
# ------------------------------------------------------------

# Definition:
# next() is used to get the next value from a generator.

def values():
    yield 100
    yield 200
    yield 300


g = values()

print(next(g))
print(next(g))
print(next(g))

# If we call next(g) again:
# print(next(g))
#
# It will give:
# StopIteration
#
# because there are no more values.


# ------------------------------------------------------------
# 5. GENERATOR STATE
# ------------------------------------------------------------

# A generator remembers its state.
# It continues execution from where it stopped.

def test():
    print("First")
    yield 1

    print("Second")
    yield 2

    print("Third")
    yield 3


g = test()

print(next(g))
print(next(g))
print(next(g))


# Output:
# First
# 1
# Second
# 2
# Third
# 3


# ------------------------------------------------------------
# 6. GENERATOR WITH for LOOP
# ------------------------------------------------------------

def numbers():
    for i in range(1, 6):
        yield i


for value in numbers():
    print(value)


# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# 7. GENERATING EVEN NUMBERS
# ------------------------------------------------------------

def even_numbers(n):
    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)


# Output:
# 2
# 4
# 6
# 8
# 10


# ------------------------------------------------------------
# 8. INFINITE GENERATOR
# ------------------------------------------------------------

# Definition:
# An infinite generator can generate values continuously.
# We can use while True.

def infinite_numbers():

    n = 1

    while True:
        yield n
        n += 1


g = infinite_numbers()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# 9. INFINITE EVEN NUMBER GENERATOR
# ------------------------------------------------------------

def infinite_even_numbers():

    n = 2

    while True:
        yield n
        n += 2


g = infinite_even_numbers()

for i in range(5):
    print(next(g))


# Output:
# 2
# 4
# 6
# 8
# 10


# ------------------------------------------------------------
# 10. GENERATOR WITH CONDITION
# ------------------------------------------------------------

def even_numbers(n):

    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i


for number in even_numbers(20):
    print(number)


# ------------------------------------------------------------
# 11. GENERATOR EXPRESSION
# ------------------------------------------------------------

# Definition:
# A generator expression is a short way to create a generator.
#
# Syntax:
# (expression for variable in sequence)

g = (x * 2 for x in range(1, 6))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# Output:
# 2
# 4
# 6
# 8
# 10


# ------------------------------------------------------------
# 12. GENERATOR EXPRESSION WITH for LOOP
# ------------------------------------------------------------

g = (x * 2 for x in range(1, 6))

for value in g:
    print(value)


# ------------------------------------------------------------
# 13. LIST COMPREHENSION vs GENERATOR EXPRESSION
# ------------------------------------------------------------

# List comprehension
numbers_list = [x * 2 for x in range(1, 6)]

print(numbers_list)


# Generator expression
numbers_generator = (x * 2 for x in range(1, 6))

for value in numbers_generator:
    print(value)


# List uses []
# Generator uses ()
#
# List:
# Creates all values immediately.
#
# Generator:
# Creates values one at a time.


# ------------------------------------------------------------
# 14. LAZY EVALUATION
# ------------------------------------------------------------

# Definition:
# Lazy evaluation means a value is generated only
# when it is requested.

def lazy_numbers():

    for i in range(1, 6):
        print("Generating:", i)
        yield i


g = lazy_numbers()

print(next(g))
print(next(g))


# Only two values are generated because
# we requested only two values.


# ------------------------------------------------------------
# 15. GENERATOR FOR FACTORS
# ------------------------------------------------------------

# Definition:
# A factor is a number that divides another number
# without leaving a remainder.
#
# Example:
# Factors of 12 = 1, 2, 3, 4, 6, 12

def factors(n):

    for i in range(1, n + 1):

        if n % i == 0:
            yield i


for factor in factors(12):
    print(factor)


# Output:
# 1
# 2
# 3
# 4
# 6
# 12


# ------------------------------------------------------------
# 16. FACTORS USING GENERATOR EXPRESSION
# ------------------------------------------------------------

n = 12

factors = (i for i in range(1, n + 1) if n % i == 0)

for factor in factors:
    print(factor)


# ------------------------------------------------------------
# 17. PRIME NUMBER GENERATOR
# ------------------------------------------------------------

# Definition:
# A prime number is a number that has exactly two factors:
# 1 and itself.
#
# Examples:
# 2, 3, 5, 7, 11, 13, 17, 19

def prime_numbers(limit):

    for num in range(2, limit + 1):

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num


for prime in prime_numbers(20):
    print(prime)


# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19


# ------------------------------------------------------------
# 18. GENERATOR FOR STRINGS
# ------------------------------------------------------------

def names():

    yield "Rahul"
    yield "Raj"
    yield "Aman"


for name in names():
    print(name)


# ------------------------------------------------------------
# 19. CONVERT GENERATOR INTO LIST
# ------------------------------------------------------------

def numbers():

    yield 10
    yield 20
    yield 30


g = numbers()

result = list(g)

print(result)


# Output:
# [10, 20, 30]


# ------------------------------------------------------------
# 20. GENERATOR CAN BE USED ONLY ONCE
# ------------------------------------------------------------

def values():

    yield 1
    yield 2
    yield 3


g = values()

for value in g:
    print(value)

# Generator is now exhausted.

for value in g:
    print(value)

# Nothing will be printed the second time.


# ------------------------------------------------------------
# 21. PRACTICAL EXAMPLE - READING FILE
# ------------------------------------------------------------

# Generators are useful for reading large files
# one line at a time.

def read_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line


# Example:
#
# for line in read_file("data.txt"):
#     print(line.strip())


# ------------------------------------------------------------
# 22. return vs yield
# ------------------------------------------------------------

# return:
# - Returns a value
# - Ends the function
# - Usually used in normal functions
#
# yield:
# - Produces a value
# - Pauses the function
# - Preserves the execution state
# - Used in generator functions


def example_return():

    return 10


def example_yield():

    yield 10
    yield 20


# ------------------------------------------------------------
# 23. IMPORTANT DIFFERENCES
# ------------------------------------------------------------

# Normal function:
#
# def function():
#     return [1, 2, 3, 4, 5]
#
# Complete result is created at once.


# Generator function:
#
# def function():
#     yield 1
#     yield 2
#     yield 3
#
# Values are created one at a time.


# ------------------------------------------------------------
# 24. IMPORTANT TERMS
# ------------------------------------------------------------

# Generator:
# A function that produces values one at a time.


# yield:
# Produces a value and pauses execution.


# next():
# Retrieves the next value from a generator.


# Lazy Evaluation:
# Values are calculated only when required.


# Generator Expression:
# Short way to create a generator.


# StopIteration:
# Exception raised when the generator has no more values.


# ------------------------------------------------------------
# 25. INTERVIEW EXAMPLE
# ------------------------------------------------------------

def interview_example():

    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3


g = interview_example()

print(next(g))
print(next(g))
print(next(g))


# Execution:
#
# First next():
# A
# 1
#
# Second next():
# B
# 2
#
# Third next():
# C
# 3


# ============================================================
#                  QUICK REVISION
# ============================================================

# Generator
#     |
#     v
# Uses yield
#     |
#     v
# Produces one value at a time
#     |
#     v
# next() requests next value
#     |
#     v
# Generator pauses at yield
#     |
#     v
# Remembers its state
#     |
#     v
# Continues from where it stopped


# MOST IMPORTANT SYNTAX:
#
# def generator():
#     yield value
#
#
# Get values:
#
# g = generator()
# print(next(g))
#
#
# Using loop:
#
# for value in generator():
#     print(value)
#
#
# Generator expression:
#
# g = (x for x in range(10))
#
#
# Infinite generator:
#
# def numbers():
#     n = 1
#
#     while True:
#         yield n
#         n += 1


# ============================================================
# KEY TAKEAWAY
# ============================================================

# A generator uses 'yield' to produce values one at a time.
#
# It remembers its execution state between calls.
#
# Generators save memory because they do not create
# the complete sequence at once.
#
# Generators are especially useful for:
# - Large data
# - File processing
# - Data streams
# - Infinite sequences
# - Lazy evaluation
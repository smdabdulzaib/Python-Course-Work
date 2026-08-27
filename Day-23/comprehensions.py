
# ============================================================
#                 PYTHON COMPREHENSIONS
# ============================================================

# Definition:
# Comprehension is a short and simple way to create
# a new collection from an existing iterable.
#
# Comprehensions make code more concise and readable.
#
# Types of comprehensions:
# 1. List Comprehension
# 2. Set Comprehension
# 3. Dictionary Comprehension
# 4. Generator Expression
#
# In this topic, we mainly focus on:
# List Comprehension
# Set Comprehension
# Conditions
# Nested Comprehensions
# 2D Lists
# Data Transformation


# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

# Definition:
# List comprehension is a short way to create a list
# using a single line of code.

# Normal method:

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# Using list comprehension:

numbers = [i for i in range(1, 6)]

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# Syntax:
#
# [expression for variable in iterable]


# Example:

squares = [i * i for i in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 2. LIST COMPREHENSION WITH STRINGS
# ============================================================

names = ["rahul", "raj", "aman"]

result = [name.upper() for name in names]

print(result)

# Output:
# ['RAHUL', 'RAJ', 'AMAN']


# ============================================================
# 3. LIST COMPREHENSION WITH CONDITION
# ============================================================

# Syntax:
#
# [expression for variable in iterable if condition]


# Example: Even numbers

even = [i for i in range(1, 11) if i % 2 == 0]

print(even)

# Output:
# [2, 4, 6, 8, 10]


# Example: Odd numbers

odd = [i for i in range(1, 11) if i % 2 != 0]

print(odd)

# Output:
# [1, 3, 5, 7, 9]


# ============================================================
# 4. FILTERING ELEMENTS
# ============================================================

# We can use conditions to filter values.

numbers = [10, 15, 20, 25, 30, 35]

result = [i for i in numbers if i > 20]

print(result)

# Output:
# [25, 30, 35]


# Example: Numbers divisible by 5

result = [i for i in numbers if i % 5 == 0]

print(result)

# Output:
# [10, 15, 20, 25, 30, 35]


# ============================================================
# 5. CONDITIONAL EXPRESSION
# ============================================================

# We can use if-else inside a comprehension.

# Syntax:
#
# [value_if_true if condition else value_if_false
#  for variable in iterable]


numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in numbers
]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 6. DIFFERENCE: FILTER vs IF-ELSE
# ============================================================

# Only IF:
#
# Used for FILTERING values.

numbers = [1, 2, 3, 4, 5]

result = [i for i in numbers if i % 2 == 0]

print(result)

# Output:
# [2, 4]


# IF-ELSE:
#
# Used for TRANSFORMING values.

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in numbers
]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 7. SQUARES OF NUMBERS
# ============================================================

squares = [i ** 2 for i in range(1, 11)]

print(squares)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ============================================================
# 8. CUBES OF NUMBERS
# ============================================================

cubes = [i ** 3 for i in range(1, 6)]

print(cubes)

# Output:
# [1, 8, 27, 64, 125]


# ============================================================
# 9. FACTORS OF A NUMBER
# ============================================================

# A factor divides a number without remainder.

n = 12

factors = [i for i in range(1, n + 1) if n % i == 0]

print(factors)

# Output:
# [1, 2, 3, 4, 6, 12]


# ============================================================
# 10. PRIME NUMBERS
# ============================================================

# A prime number has exactly two factors:
# 1 and itself.

primes = []

for num in range(2, 21):

    factors = [i for i in range(1, num + 1) if num % i == 0]

    if len(factors) == 2:
        primes.append(num)

print(primes)

# Output:
# [2, 3, 5, 7, 11, 13, 17, 19]


# ============================================================
# 11. SET COMPREHENSION
# ============================================================

# Definition:
# Set comprehension is used to create a set
# in a short way.
#
# Syntax:
#
# {expression for variable in iterable}


numbers = [1, 2, 2, 3, 3, 4, 5, 5]

result = {i for i in numbers}

print(result)

# Output:
# {1, 2, 3, 4, 5}


# Sets automatically remove duplicate values.


# Example:

squares = {i ** 2 for i in range(1, 6)}

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# ============================================================
# 12. SET COMPREHENSION WITH CONDITION
# ============================================================

numbers = range(1, 11)

even = {i for i in numbers if i % 2 == 0}

print(even)

# Output:
# {2, 4, 6, 8, 10}


# ============================================================
# 13. NESTED LIST COMPREHENSION
# ============================================================

# Definition:
# A comprehension containing another loop
# is called a nested comprehension.

result = [
    i * j
    for i in range(1, 4)
    for j in range(1, 4)
]

print(result)

# Output:
# [1, 2, 3, 2, 4, 6, 3, 6, 9]


# ============================================================
# 14. FLATTENING A NESTED LIST
# ============================================================

# Nested list:

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Normal method:

result = []

for row in numbers:
    for value in row:
        result.append(value)

print(result)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Using list comprehension:

result = [value for row in numbers for value in row]

print(result)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================================
# 15. CREATING A 2D LIST
# ============================================================

# We can create a 2D list using nested comprehension.

matrix = [
    [0 for j in range(3)]
    for i in range(3)
]

print(matrix)

# Output:
# [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]


# ============================================================
# 16. CREATING A 2D LIST WITH NUMBERS
# ============================================================

matrix = [
    [j for j in range(1, 4)]
    for i in range(3)
]

print(matrix)

# Output:
# [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ]


# ============================================================
# 17. MULTIPLICATION TABLE USING COMPREHENSION
# ============================================================

table = [
    i * j
    for i in range(1, 4)
    for j in range(1, 4)
]

print(table)

# Output:
# [1, 2, 3, 2, 4, 6, 3, 6, 9]


# ============================================================
# 18. MULTIPLE CONDITIONS
# ============================================================

numbers = range(1, 21)

result = [
    i
    for i in numbers
    if i % 2 == 0
    if i > 10
]

print(result)

# Output:
# [12, 14, 16, 18, 20]


# ============================================================
# 19. STRING FILTERING
# ============================================================

names = ["Rahul", "Aman", "Raj", "Abdul", "Ravi"]

result = [
    name
    for name in names
    if name.startswith("A")
]

print(result)

# Output:
# ['Aman', 'Abdul']


# ============================================================
# 20. TRANSFORMING LIST ELEMENTS
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = [i * 10 for i in numbers]

print(result)

# Output:
# [10, 20, 30, 40, 50]


# ============================================================
# 21. CONVERT STRINGS TO UPPERCASE
# ============================================================

names = ["rahul", "aman", "raj"]

result = [name.upper() for name in names]

print(result)

# Output:
# ['RAHUL', 'AMAN', 'RAJ']


# ============================================================
# 22. REMOVE EMPTY STRINGS
# ============================================================

data = ["Python", "", "Java", "", "SQL", "HTML"]

result = [value for value in data if value != ""]

print(result)

# Output:
# ['Python', 'Java', 'SQL', 'HTML']


# ============================================================
# 23. TAKING MULTIPLE USER INPUTS
# ============================================================

# input() returns a string.
# split() separates the input.
# int() converts each value into an integer.

numbers = [
    int(x)
    for x in input("Enter numbers: ").split()
]

print(numbers)


# Example input:
# Enter numbers: 10 20 30 40
#
# Output:
# [10, 20, 30, 40]


# ============================================================
# 24. MULTIPLE INPUTS AND SQUARES
# ============================================================

numbers = [
    int(x)
    for x in input("Enter numbers: ").split()
]

squares = [x ** 2 for x in numbers]

print(squares)


# Input:
# 1 2 3 4 5
#
# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 25. MULTIPLE INPUTS AND EVEN NUMBERS
# ============================================================

numbers = [
    int(x)
    for x in input("Enter numbers: ").split()
]

even = [x for x in numbers if x % 2 == 0]

print(even)


# Input:
# 10 15 20 25 30
#
# Output:
# [10, 20, 30]


# ============================================================
# 26. MULTIPLE USER NAMES
# ============================================================

names = input("Enter names: ").split()

result = [name.upper() for name in names]

print(result)


# Input:
# rahul raj aman
#
# Output:
# ['RAHUL', 'RAJ', 'AMAN']


# ============================================================
# 27. DICTIONARY COMPREHENSION
# ============================================================

# Definition:
# Dictionary comprehension is used to create dictionaries
# in a short way.
#
# Syntax:
#
# {key: value for variable in iterable}


numbers = range(1, 6)

squares = {
    i: i ** 2
    for i in numbers
}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 28. DICTIONARY COMPREHENSION WITH CONDITION
# ============================================================

numbers = range(1, 11)

even_squares = {
    i: i ** 2
    for i in numbers
    if i % 2 == 0
}

print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ============================================================
# 29. LIST COMPREHENSION VS NORMAL FOR LOOP
# ============================================================

# Normal for loop:

result = []

for i in range(1, 6):
    result.append(i * 2)

print(result)


# List comprehension:

result = [i * 2 for i in range(1, 6)]

print(result)


# Both produce:
# [2, 4, 6, 8, 10]


# ============================================================
# 30. GENERAL SYNTAX
# ============================================================

# Basic:

# [expression for variable in iterable]


# With condition:

# [expression for variable in iterable if condition]


# With if-else:

# [value_if_true if condition else value_if_false
#  for variable in iterable]


# Nested:

# [expression
#  for variable1 in iterable1
#  for variable2 in iterable2]


# ============================================================
# 31. IMPORTANT DIFFERENCE
# ============================================================

# FILTERING:

numbers = [1, 2, 3, 4, 5]

result = [i for i in numbers if i > 3]

print(result)

# Output:
# [4, 5]


# TRANSFORMATION:

result = [i * 10 for i in numbers]

print(result)

# Output:
# [10, 20, 30, 40, 50]


# CONDITIONAL TRANSFORMATION:

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in numbers
]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 32. IMPORTANT POINTS TO REMEMBER
# ============================================================

# 1. List comprehension uses []
#
# 2. Set comprehension uses {}
#
# 3. Dictionary comprehension uses {key: value}
#
# 4. Generator expression uses ()
#
# 5. 'if' at the end is generally used for filtering.
#
# 6. 'if-else' before the for is used for transformation.
#
# 7. Nested comprehensions can contain multiple loops.
#
# 8. Comprehensions make code shorter.
#
# 9. Readability is more important than making code
#    unnecessarily short.


# ============================================================
#                    QUICK REVISION
# ============================================================

# LIST COMPREHENSION
#
# [expression for variable in iterable]


# Example:

numbers = [i for i in range(1, 6)]


# WITH CONDITION:

even = [i for i in range(1, 11) if i % 2 == 0]


# IF-ELSE:

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
]


# SET COMPREHENSION:

result = {i for i in range(1, 6)}


# DICTIONARY COMPREHENSION:

result = {
    i: i ** 2
    for i in range(1, 6)
}


# NESTED COMPREHENSION:

result = [
    value
    for row in matrix
    for value in row
]


# ============================================================
#                    KEY TAKEAWAY
# ============================================================

# Comprehensions provide a concise way to create
# collections in Python.
#
# They are useful for:
#
# 1. Creating lists
# 2. Filtering data
# 3. Transforming data
# 4. Creating sets
# 5. Creating dictionaries
# 6. Working with nested lists
# 7. Creating 2D lists
# 8. Processing multiple inputs
#
# Always remember:
#
# Readability > Short code
#
# Do not use comprehensions when they make the code
# difficult to understand.


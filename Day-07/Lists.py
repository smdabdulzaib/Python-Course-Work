# ============================================================
# PYTHON LISTS - BASICS
# ============================================================

# ============================================================
# 1. What is a List?
# ============================================================
# Definition:
# A list is a built-in data type in Python that stores
# multiple items in a single variable.
#
# Features:
# • Ordered
# • Mutable (can be changed)
# • Allows duplicate values
# • Can store different data types

# Syntax:
# list_name = [item1, item2, item3]


# ============================================================
# 2. Creating a List
# ============================================================

# Empty List
l = []

print(l)

# Output:
# []


# ------------------------------------------------------------
# Another way to create an empty list
# ------------------------------------------------------------

l = list()

print(l)

# Output:
# []


# ============================================================
# Wrong Syntax
# ============================================================

# Wrong:
# l = {]

# Error:
# SyntaxError:
# closing parenthesis ']' does not match opening parenthesis '{'


# ============================================================
# 3. List with Different Data Types
# ============================================================

l = [
    1,                      # Integer
    12.3,                   # Float
    2 + 3j,                 # Complex Number
    "str",                  # String
    [1, 2, 3],              # Nested List
    (1, 2, 23),             # Tuple
    {1: 1, 2: 2, 3: 4}      # Dictionary
]

print(l)

# Output:
# [1, 12.3, (2+3j), 'str',
#  [1, 2, 3], (1, 2, 23),
#  {1: 1, 2: 2, 3: 4}]


# ============================================================
# 4. List Allows Duplicate Values
# ============================================================

l = [1, 1, 2, 3]

print(l)

# Output:
# [1, 1, 2, 3]

# Duplicate values are allowed.


# ============================================================
# 5. type()
# ============================================================
# Definition:
# type() returns the data type of a variable.

print(type(l))

# Output:
# <class 'list'>


# ============================================================
# 6. Sample List
# ============================================================

l = [1, 2, 3, 4, 5]

print(l)

# Output:
# [1, 2, 3, 4, 5]


# ============================================================
# 7. List Slicing
# ============================================================
# Syntax:
# list[start : stop : step]


# Reverse the List
print(l[::-1])

# Output:
# [5, 4, 3, 2, 1]


# ------------------------------------------------------------
# First Three Elements
# ------------------------------------------------------------

print(l[:3])

# Output:
# [1, 2, 3]


# ------------------------------------------------------------
# Elements from Index 1 to Index 3
# ------------------------------------------------------------

print(l[1:4])

# Output:
# [2, 3, 4]


# ============================================================
# 8. Membership Operators
# ============================================================
# Definition:
# Used to check whether an element exists in a list.
#
# in
# not in


print(2 in l)

# Output:
# True


print(3 in l)

# Output:
# True


print(10 in l)

# Output:
# False


print(10 not in l)

# Output:
# True


print(1 not in l)

# Output:
# False


# ============================================================
# SUMMARY
# ============================================================

# List
# ----
# Ordered collection
# Mutable
# Allows duplicates
# Can store different data types


# Create Empty List
# -----------------
# l = []
# OR
# l = list()


# Reverse List
# ------------
# l[::-1]


# Slicing
# -------
# l[:3]
# First three elements

# l[1:4]
# Elements from index 1 to 3


# Membership Operators
# --------------------
# in
# not in

# Example:
# 2 in l          -> True
# 10 in l         -> False
# 10 not in l     -> True


# ============================================================
# END OF NOTES
# ============================================================
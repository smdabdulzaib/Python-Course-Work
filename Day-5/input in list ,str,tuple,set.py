# ============================================================
# PYTHON INPUT FUNCTIONS - CLASS NOTES
# ============================================================

# ============================================================
# 1. input()
# ============================================================
# Definition:
# input() takes input from the user.
# By default, it always returns a STRING.

x = input()

# Input:
# jsomsub

# Output:
# >>> x
# 'jsomsub'


# ------------------------------------------------------------

name = input()

# Input:
# zaib

# Output:
# >>> name
# 'zaib'


# ------------------------------------------------------------

age = input()

# Input:
# 21

# Output:
# >>> age
# '21'

# Notice:
# Even though you entered 21, Python stores it as a string.


# ============================================================
# 2. int(input())
# ============================================================
# Definition:
# Converts the input string into an integer.

age = int(input())

# Input:
# 21

# Output:
# >>> age
# 21


# ------------------------------------------------------------

age = int(input("Enter age: "))

# Input:
# Enter age: 22

# Output:
# >>> age
# 22


# ============================================================
# 3. float(input())
# ============================================================
# Definition:
# Converts the input into a floating-point number.

price = float(input())

# Input:
# 2.034

# Output:
# >>> price
# 2.034


# ============================================================
# 4. Taking String Input
# ============================================================

names = input("Enter names: ")

# Input:
# zaib sajid

# Output:
# >>> names
# 'zaib sajid'

# Entire input is stored as one string.


# ============================================================
# 5. split()
# ============================================================
# Definition:
# split() separates a string into words using spaces.
# It returns a LIST.

names = input("Enter: ").split()

# Input:
# zaib sajid

# Output:
# >>> names
# ['zaib', 'sajid']


# ============================================================
# 6. List of Numbers
# ============================================================
# Without map()

numbers = input("Enter: ").split()

# Input:
# 22 3 34 4

# Output:
# >>> numbers
# ['22', '3', '34', '4']

# These are STRINGS, not integers.


# ============================================================
# Wrong Method
# ============================================================

# numbers = int(input("Enter: ").split())

# Input:
# 22 3 12

# Error:
# TypeError:
# int() cannot convert a list into an integer.


# ============================================================
# Another Wrong Method
# ============================================================

# numbers = int(input())

# Input:
# 22 34 231 12

# Error:
# ValueError:
# int() expects only one integer.


# ============================================================
# 7. map()
# ============================================================
# Definition:
# map() applies a function to every element.

numbers = map(int, input("Enter: ").split())

# Input:
# 2 232 1434

# Output:
# >>> numbers
# <map object>

# map() returns a map object.


# ============================================================
# Convert map object into list
# ============================================================

numbers = list(map(int, input("Enter: ").split()))

# Input:
# 2 232 4 12

# Output:
# >>> numbers
# [2, 232, 4, 12]


# ============================================================
# 8. tuple()
# ============================================================
# Definition:
# tuple() creates an immutable collection.

names = tuple(input().split())

# Input:
# zaib

# Output:
# >>> names
# ('zaib',)


# ------------------------------------------------------------

numbers = tuple(map(int, input("Enter: ").split()))

# Input:
# 1 223 43

# Output:
# >>> numbers
# (1, 223, 43)


# ============================================================
# 9. set()
# ============================================================
# Definition:
# A set stores only UNIQUE values.
# Duplicate values are automatically removed.

names = set(input().split())

# Input:
# hi jid d d

# Output:
# >>> names
# {'hi', 'jid', 'd'}

# Duplicate 'd' is removed.


# ============================================================
# Another Example
# ============================================================

k = tuple(map(int, input("Enter: ").split()))

# Input:
# 2 34 5 3

# Output:
# >>> k
# (2, 34, 5, 3)


# ============================================================
# 10. Multiple Inputs
# ============================================================

a, b = [1, 2]

# Output:
# >>> a
# 1

# >>> b
# 2


# ============================================================
# Wrong Method
# ============================================================

# a, b, c = int(input().split())

# Error:
# TypeError


# ============================================================
# Correct Method
# ============================================================

a, b, c = list(map(int, input().split()))

# Input:
# 1 2 3

# Output:
# >>> a
# 1

# >>> b
# 2

# >>> c
# 3


# ============================================================
# Multiple String Inputs
# ============================================================

name, loc = input().split()

# Input:
# nnqa jhij

# Output:
# >>> name
# 'nnqa'

# >>> loc
# 'jhij'


# ============================================================
# String + Number
# ============================================================

name, age = input().split()

# Input:
# zaib 2

# Output:
# >>> name
# 'zaib'

# >>> age
# '2'

# Convert age into integer

age = int(age)

# Output:
# >>> age
# 2


# ============================================================
# 11. eval()
# ============================================================
# Definition:
# eval() evaluates the entered input as a Python expression.

e = eval(input())

# Input:
# 1

# Output:
# >>> e
# 1


# ------------------------------------------------------------

es = eval(input())

# Input:
# 1234.14

# Output:
# >>> es
# 1234.14


# ------------------------------------------------------------

e = eval(input())

# Input:
# "zaib"

# Output:
# >>> e
# 'zaib'


# ------------------------------------------------------------

m = eval(input())

# Input:
# 2+2*4+6*6+3

# Calculation:
# 2 + 8 + 36 + 3 = 49

# Output:
# >>> m
# 49


# ============================================================
# SUMMARY
# ============================================================

# input()
# --------
# Returns string.

# int(input())
# ------------
# Returns integer.

# float(input())
# --------------
# Returns float.

# split()
# -------
# Splits string into list.

# map()
# -----
# Applies function to every element.

# list(map(int, input().split()))
# -------------------------------
# Takes multiple integers as a list.

# tuple()
# -------
# Immutable collection.

# set()
# -----
# Unique values only.

# eval()
# ------
# Evaluates Python expressions.
# Example:
# Input: 2+3*4
# Output: 14

# ============================================================
# END OF NOTES
# ============================================================
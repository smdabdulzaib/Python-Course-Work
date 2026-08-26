# ============================================================
# PYTHON STRINGS - SLICING & MEMBERSHIP OPERATORS
# ============================================================

# ============================================================
# 1. String Concatenation (+)
# ============================================================
# Definition:
# Concatenation joins two or more strings into one string.

s = "codegnan" + "hyd"

# Output:
# >>> s
# 'codegnanhyd'


# ============================================================
# 2. String Repetition (*)
# ============================================================
# Definition:
# The * operator repeats a string multiple times.

s = "zaib" * 10

# Output:
# >>> s
# 'zaibzaibzaibzaibzaibzaibzaibzaibzaibzaib'


# ============================================================
# 3. Creating a String
# ============================================================

s = "zaib sajid are here"

# Output:
# >>> s
# 'zaib sajid are here'


# ============================================================
# 4. Indexing
# ============================================================
# Definition:
# Indexing is used to access a single character.
#
# Positive Index:
# Starts from 0 (left to right)
#
# Negative Index:
# Starts from -1 (right to left)

# String:
# z a i b   s a j i d   a r e   h e r e
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

print(s[1])

# Output:
# 'a'


print(s[3])

# Output:
# 'b'


print(s[-1])

# Output:
# 'e'


# ============================================================
# 5. Slicing
# ============================================================
# Definition:
# Slicing extracts part of a string.
#
# Syntax:
# string[start : stop : step]
#
# start -> Starting index
# stop  -> Ending index (not included)
# step  -> Jump value


print(s[0:4])

# Output:
# 'zaib'


# ------------------------------------------------------------

print(s[1:])

# Output:
# 'aib sajid are here'

# Starts from index 1 and goes till the end.


# ------------------------------------------------------------

print(s[:])

# Output:
# 'zaib sajid are here'

# Copies the entire string.


# ============================================================
# 6. Reverse String
# ============================================================

print(s[::-1])

# Output:
# 'ereh era dijas biaz'

# step = -1 reverses the string.


# ============================================================
# 7. Step Value
# ============================================================

print(s[::2])

# Output:
# 'zi ai r ee'

# Takes every second character.


# ============================================================
# 8. Negative Slicing
# ============================================================

print(s[-1:-5:-1])

# Output:
# 'ereh'

# Explanation:
# Starts from the last character and moves backwards.


# ------------------------------------------------------------
# Wrong Examples
# ------------------------------------------------------------

# print(s[-1:-5])

# Output:
# ''

# Reason:
# Default step is +1.
# Python cannot move forward from -1 to -5.


# ------------------------------------------------------------

# print(s[-1:-2])

# Output:
# ''

# Same reason:
# Step is +1.


# ============================================================
# 9. Membership Operators
# ============================================================
# Definition:
# Used to check whether a value exists in a string.
#
# in      -> Returns True if found.
# not in  -> Returns True if NOT found.


print("zaib" in s)

# Output:
# True


print("sajid" in s)

# Output:
# True


print("kin" not in s)

# Output:
# True


print("i" in s)

# Output:
# True


print("o" in s)

# Output:
# False


# ============================================================
# Common Syntax Errors
# ============================================================

# Wrong:
# s[::}

# Error:
# SyntaxError:
# closing parenthesis '}' does not match '['


# ------------------------------------------------------------

# Wrong:
# s = [-1:-5:-1]

# Error:
# SyntaxError

# Reason:
# Slicing works only on an existing sequence.
# Correct:
# s[-1:-5:-1]


# ------------------------------------------------------------

# Wrong:
# ''sajid'' in s

# Error:
# SyntaxError

# Correct:
# "sajid" in s


# ------------------------------------------------------------

# Wrong:
# "i" in s:

# Error:
# SyntaxError

# Reason:
# Colon (:) is only used after statements like
# if, for, while, def, class, etc.

# Correct:
# "i" in s


# ============================================================
# SUMMARY
# ============================================================

# String Concatenation
# --------------------
# +
# Example:
# "abc" + "xyz"
# Output:
# 'abcxyz'


# String Repetition
# -----------------
# *
# Example:
# "Hi" * 3
# Output:
# 'HiHiHi'


# Indexing
# --------
# Positive:
# s[0]

# Negative:
# s[-1]


# Slicing
# -------
# s[start:stop]

# s[:]
# Entire string

# s[::-1]
# Reverse string

# s[::2]
# Every second character


# Membership Operators
# --------------------
# in
# not in

# Example:
# "abc" in s

# Returns:
# True or False


# ============================================================
# END OF NOTES
# ============================================================




"""Concept	Syntax	Example	Output
Concatenation	+	"a" + "b"	'ab'
Repetition	*	"Hi"*3	'HiHiHi'
Indexing	s[i]	s[0]	First character
Negative Index	s[-1]	s[-1]	Last character
Slicing	s[start:stop]	s[0:4]	'zaib'
Reverse	s[::-1]	s[::-1]	Reversed string
Step	s[::2]	s[::2]	Every second character
Membership	in	"zaib" in s	True
Not Membership	not in	"kin" not in s	True"""
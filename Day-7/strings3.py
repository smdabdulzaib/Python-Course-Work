# ============================================================
# PYTHON STRING CHECKING METHODS
# ============================================================

# ============================================================
# 1. startswith()
# ============================================================
# Definition:
# startswith() checks whether a string starts with
# the given characters.
#
# Syntax:
# string.startswith("text")

c = "string.py"

print(c.startswith("str"))

# Output:
# True


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# c.startwith("str")

# Error:
# AttributeError:
# 'str' object has no attribute 'startwith'

# Correct:
# c.startswith("str")


# ============================================================
# 2. endswith()
# ============================================================
# Definition:
# endswith() checks whether a string ends with
# the given characters.
#
# Syntax:
# string.endswith("text")

print(c.endswith("py"))

# Output:
# True


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# c.endswith(.py)

# Error:
# SyntaxError

# Correct:
# c.endswith("py")


# ============================================================
# 3. islower()
# ============================================================
# Definition:
# Returns True if all alphabet characters
# are lowercase.

print(c.islower())

# Output:
# True


# ============================================================
# 4. isupper()
# ============================================================
# Definition:
# Returns True if all alphabet characters
# are uppercase.

print(c.isupper())

# Output:
# False


print("PYTHON".isupper())

# Output:
# True


# ============================================================
# 5. isalpha()
# ============================================================
# Definition:
# Returns True if the string contains
# only alphabet letters (A-Z or a-z).

print(c.isalpha())

# Output:
# False

# Reason:
# "string.py" contains "."


k = "zaib"

print(k.isalpha())

# Output:
# True


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# c.isapha()
# k.isaplha()

# Error:
# AttributeError

# Correct:
# isalpha()


# ============================================================
# 6. isalnum()
# ============================================================
# Definition:
# Returns True if the string contains
# only letters and numbers.
#
# No spaces or special characters are allowed.

m = "pyth22"

print(m.isalnum())

# Output:
# True


print("s123".isalnum())

# Output:
# True


print("s.123".isalnum())

# Output:
# False

# Reason:
# '.' is a special character.


# ============================================================
# 7. isspace()
# ============================================================
# Definition:
# Returns True if the string contains
# only whitespace characters.

print("   ".isspace())

# Output:
# True


# ============================================================
# 8. istitle()
# ============================================================
# Definition:
# Returns True if every word starts
# with a capital letter.

print("this is title".istitle())

# Output:
# False


print("Kng Ljnf INi".istitle())

# Output:
# False

# Reason:
# "INi" is not in title case.


print("This Is Title".istitle())

# Output:
# True


# ============================================================
# 9. isidentifier()
# ============================================================
# Definition:
# Checks whether a string is a valid
# Python identifier (variable name).

print("my@identi".isidentifier())

# Output:
# False

# Reason:
# '@' is not allowed.


print("my_is".isidentifier())

# Output:
# True


# More Examples

print("student1".isidentifier())

# Output:
# True


print("1student".isidentifier())

# Output:
# False

# Variable names cannot start with a digit.


print("my name".isidentifier())

# Output:
# False

# Spaces are not allowed.


# ============================================================
# Common Errors
# ============================================================

# Wrong:
# c.startwith("str")

# Correct:
# c.startswith("str")


# ------------------------------------------------------------

# Wrong:
# c.isapha()

# Correct:
# c.isalpha()


# ------------------------------------------------------------

# Wrong:
# k.isaplha()

# Correct:
# k.isalpha()


# ------------------------------------------------------------

# Wrong:
# "mu

# Error:
# SyntaxError:
# Unterminated string literal

# Reason:
# Closing quotation mark is missing.


# ============================================================
# SUMMARY
# ============================================================

# startswith()
# ------------
# Checks starting characters.
#
# Example:
# "python".startswith("py")
# Output:
# True


# endswith()
# ----------
# Checks ending characters.
#
# Example:
# "python.py".endswith("py")
# Output:
# True


# islower()
# ---------
# All letters are lowercase.


# isupper()
# ---------
# All letters are uppercase.


# isalpha()
# ---------
# Only letters.


# isalnum()
# ---------
# Only letters and numbers.


# isspace()
# ---------
# Only spaces.


# istitle()
# ---------
# Every word starts with a capital letter.


# isidentifier()
# --------------
# Valid Python variable name.


# ============================================================
# END OF NOTES
# ============================================================
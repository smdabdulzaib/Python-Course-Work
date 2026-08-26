# ============================================================
# PYTHON LIST METHODS
# ============================================================

# ============================================================
# 1. append()
# ============================================================
# Definition:
# append() adds ONE element at the end of the list.
#
# Syntax:
# list.append(item)

a = [1, 2, 3, 4, 4, 5, 767, 76]

a.append(443)

print(a)

# Output:
# [1, 2, 3, 4, 4, 5, 767, 76, 443]


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# a.append(79, 44)

# Error:
# TypeError:
# append() takes exactly one argument.

# Correct:
# a.append(79)
# OR
# a.extend([79, 44])


# ============================================================
# 2. insert()
# ============================================================
# Definition:
# insert() adds an element at a specified index.
#
# Syntax:
# list.insert(index, value)

a.insert(1, 112230)

print(a)

# Output:
# [1, 112230, 2, 3, 4, 4, 5, 767, 76, 443]


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# a.insert[1,1111]

# Error:
# TypeError

# Correct:
# a.insert(1,1111)


# ============================================================
# 3. extend()
# ============================================================
# Definition:
# extend() adds multiple elements to a list.
#
# Syntax:
# list.extend(iterable)

a.extend([25, 22, 342, 34, 123])

print(a)

# Output:
# [1, 112230, 2, 3, 4, 4, 5, 767,
# 76, 443, 25, 22, 342, 34, 123]


# ============================================================
# 4. Update an Element
# ============================================================
# Definition:
# Replace an existing value using its index.

a[2] = 212121213

print(a)

# Output:
# [1, 112230, 212121213, 3, 4, 4,
# 5, 767, 76, 443, 25, 22, 342, 34, 123]


# ============================================================
# 5. pop()
# ============================================================
# Definition:
# pop() removes and returns an element.
#
# Without index:
# Removes the last element.

print(a.pop())

# Output:
# 123


# With index:
print(a.pop(1))

# Output:
# 112230


# ------------------------------------------------------------
# Wrong Method
# ------------------------------------------------------------

# a,pop(1)

# Error:
# NameError

# Correct:
# a.pop(1)


# ============================================================
# 6. remove()
# ============================================================
# Definition:
# remove() removes the FIRST occurrence of a value.

a.remove(1)

print(a)

# Output:
# [212121213, 3, 4, 4, 5, 767,
# 76, 443, 25, 22, 342, 34]


# ============================================================
# 7. del
# ============================================================
# Definition:
# del deletes an element using its index.

del a[1]

print(a)

# Output:
# [212121213, 4, 4, 5, 767,
# 76, 443, 25, 22, 342, 34]


# ============================================================
# 8. clear()
# ============================================================
# Definition:
# clear() removes all elements.

a.clear()

print(a)

# Output:
# []


# ============================================================
# 9. max()
# ============================================================
# Definition:
# Returns the largest element.

m = [1, 3, 4, 5, 7, 3, 2, 5, 7, 2]

print(max(m))

# Output:
# 7


# If list is empty

# max(a)

# Error:
# ValueError:
# max() iterable argument is empty


# ============================================================
# 10. min()
# ============================================================

print(min(m))

# Output:
# 1


# ============================================================
# 11. sorted()
# ============================================================
# Definition:
# Returns a NEW sorted list.
# Original list remains unchanged.

print(sorted(m))

# Output:
# [1, 2, 2, 3, 3, 4, 5, 5, 7, 7]


# ============================================================
# 12. sort()
# ============================================================
# Definition:
# sort() sorts the ORIGINAL list.
#
# Returns None.

m.sort()

print(m)

# Output:
# [1, 2, 2, 3, 3, 4, 5, 5, 7, 7]


# ------------------------------------------------------------
# Wrong Methods
# ------------------------------------------------------------

# sort(m)

# Error:
# NameError


# m.sort().

# Error:
# SyntaxError


# Difference
# ----------
# sorted(m) -> Creates a new sorted list.
# m.sort()  -> Changes the original list.


# ============================================================
# 13. sum()
# ============================================================
# Definition:
# Returns the sum of all elements.

print(sum(m))

# Output:
# 39


# ============================================================
# 14. copy()
# ============================================================
# Definition:
# copy() creates a new list.

l = [1, 2, 3]

n = l

n.append(4)

print(n)

# Output:
# [1, 2, 3, 4]

print(l)

# Output:
# [1, 2, 3, 4]

# Both variables refer to the SAME list.


# ------------------------------------------------------------

m = l.copy()

m.append(10)

print(m)

# Output:
# [1, 2, 3, 4, 10]

print(l)

# Output:
# [1, 2, 3, 4]

# copy() creates a separate list.


# ============================================================
# 15. all()
# ============================================================
# Definition:
# Returns True only if ALL elements are True.

print(all([0, '', [], (), {}, False]))

# Output:
# False

print(all([1, '', [], (), {}, False]))

# Output:
# False


# ============================================================
# 16. any()
# ============================================================
# Definition:
# Returns True if AT LEAST ONE element is True.

print(any([1, '', [], (), {}, False]))

# Output:
# True


# ============================================================
# 17. count()
# ============================================================
# Definition:
# Counts how many times an element appears.

l = [1, 2, 3, 4, 5]

print(l.count(3))

# Output:
# 1


# ============================================================
# 18. Nested Lists
# ============================================================
# Definition:
# A list inside another list is called a nested list.

l = [
    [1, 2, 3, 4, 5],
    [7, 8, 9, 5, 53]
]

print(l[0])

# Output:
# [1, 2, 3, 4, 5]


print(l[1])

# Output:
# [7, 8, 9, 5, 53]


# Accessing elements

print(l[0][4])

# Output:
# 5


print(l[1][4])

# Output:
# 53


# ============================================================
# SUMMARY
# ============================================================

# append(x)
# ---------
# Adds one element at the end.

# insert(i, x)
# ------------
# Adds an element at index i.

# extend(iterable)
# ----------------
# Adds multiple elements.

# pop()
# -----
# Removes and returns an element.

# remove(x)
# ---------
# Removes the first occurrence of x.

# del
# ---
# Deletes an element by index.

# clear()
# -------
# Removes all elements.

# max()
# -----
# Largest element.

# min()
# -----
# Smallest element.

# sorted()
# --------
# Returns a new sorted list.

# sort()
# ------
# Sorts the original list.

# sum()
# -----
# Returns the sum of all elements.

# copy()
# -------
# Creates a separate copy of a list.

# all()
# -----
# True if all elements are True.

# any()
# -----
# True if at least one element is True.

# count()
# --------
# Counts occurrences of an element.

# Nested List
# -----------
# Access using:
# list[row][column]

# ============================================================
# END OF NOTES
# ============================================================

# PYTHON OPERATORS

# 1. Arithmetic Operators
# Definition: Arithmetic operators are used to perform mathematical operations.

a = 20
b = 10

print("Arithmetic Operators")
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)


# 2. Comparison (Relational) Operators
# Definition: Comparison operators compare two values and return True or False.

print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# 3. Assignment Operators
# Definition: Assignment operators are used to assign or update values of variables.

c = 5
print("\nAssignment Operators")
print("Initial Value:", c)

c += 5
print("c += 5 :", c)

c -= 2
print("c -= 2 :", c)

c *= 10
print("c *= 10 :", c)

c /= 5
print("c /= 5 :", c)

c //= 2
print("c //= 2 :", c)

c %= 3
print("c %= 3 :", c)

c **= 2
print("c **= 2 :", c)


# 4. Logical Operators
# Definition: Logical operators are used to combine two or more conditions.

print("\nLogical Operators")

print("AND :", a % 2 == 0 and a % 3 == 0)
print("OR  :", a % 2 == 0 or a % 3 == 0)
print("NOT :", not (a < 1))


# 5. Membership Operators
# Definition: Membership operators check whether a value exists in a collection.

print("\nMembership Operators")

s = "codegnan"
print("'e' in s :", 'e' in s)
print("'z' in s :", 'z' in s)
print("'m' not in s :", 'm' not in s)

l = [1, 2, 3, 4, 5]
print("1 in list :", 1 in l)
print("9 not in list :", 9 not in l)

t = (1, 2, 3, 4, 5)
print("1 in tuple :", 1 in t)
print("8 not in tuple :", 8 not in t)

st = {1, 2, 3, 4}
print("1 in set :", 1 in st)
print("8 not in set :", 8 not in st)

d = {"name": "zaib", "age": 22, "batch": "CSE"}
print("'name' in dictionary :", "name" in d)
print("'zaib' in dictionary :", "zaib" in d)   # Checks keys only
print("'batch' in dictionary :", "batch" in d)


# 6. Identity Operators
# Definition: Identity operators check whether two variables refer to the same object in memory.
 
print("\nIdentity Operators")
 
x = [1, 2, 3]
y = [1, 2, 3]
z = x
 
print("id(x):", id(x))
print("id(y):", id(y))
print("id(z):", id(z))
 
print("x is y :", x is y)
print("x is z :", x is z)
print("x is not y :", x is not y)
print("x is z :", z is x)
 
# 7. Bitwise Operators
# Definition: Bitwise operators perform operations on the binary representation of integers.
 
print("\nBitwise Operators")
 
print("9 & 10 =", 9 & 10)
print("9 | 10 =", 9 | 10)
print("9 ^ 10 =", 9 ^ 10)
print("~9 =", ~9)
print("8 >> 2 =", 8 >> 2)
print("8 << 2 =", 8 << 2)
 
 
# 8. Formatted String (f-string)
# Definition: An f-string is used to insert variables directly into a string.
 
marks = 200

print("\nFormatted String")
print(f"Zaib scored {marks} marks in the exam.")


print("========== PYTHON DATA TYPES ==========\n")

# ==============================
# 1. Numeric Data Types
# ==============================
print("1. Numeric Data Types")

a = 7               # int
b = 7.5             # float
c = 3 + 4j          # complex

print("Integer :", a, "Type:", type(a))
print("Float   :", b, "Type:", type(b))
print("Complex :", c, "Type:", type(c))
print()

# ==============================
# 2. Sequence Data Types
# ==============================
print("2. Sequence Data Types")

s = "King"                  # String
l = [1, 2, 3, "Lion", 1.2]  # List
t = (1, 2, "Lion")          # Tuple
r = range(5)                # Range

print("String :", s, "Type:", type(s))
print("List   :", l, "Type:", type(l))
print("Tuple  :", t, "Type:", type(t))
print("Range  :", r, "Type:", type(r))

print()

# ==============================
# 3. Mapping Data Type
# ==============================
print("3. Mapping Data Type")

d = {"name": "Zaib", "age": 22}

print("Dictionary :", d)
print("Type :", type(d))

print()

# ==============================
# 4. Set Data Types
# ==============================
print("4. Set Data Types")

st = {1, 2, 3, 4, 5}
fs = frozenset({1, 2, 3, 4})

print("Set        :", st, "Type:", type(st))
print("Frozen Set :", fs, "Type:", type(fs))

print()
 
# ==============================
# 5. Boolean Data Type
# ==============================
print("5. Boolean Data Type")
 
x = True
y = False
 
 
print("True  :", x, "Type:", type(x))
print("False :", y, "Type:", type(y))
 
print()

# ==============================
# 6. Binary Data Types
# ==============================
print("6. Binary Data Types")

b = b"Hello"
ba = bytearray(5)
mv = memoryview(bytes(5))
 
print("Bytes      :", b, "Type:", type(b))
print("Bytearray  :", ba, "Type:", type(ba))
print("Memoryview :", mv, "Type:", type(mv))
 
print()
 
# ==============================
# 7. None Data Type
# ==============================
print("7. None Data Type")
 
n = None
 
print("Value :", n)

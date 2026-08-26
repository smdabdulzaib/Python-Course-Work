
# PYTHON TYPE CONVERSIONS
# ==========================================

# ==========================
# 1. int Conversions
# ==========================
a = 10

print("INT TO FLOAT :", float(a))
print("INT TO COMPLEX :", complex(a))
print("INT TO STRING :", str(a))
print("INT TO BOOLEAN :", bool(a))

# print(list(a))      # Error
# print(tuple(a))     # Error
# print(set(a))       # Error
# print(dict(a))      # Error

print()

# ==========================
# 2. float Conversions
# ==========================
b = 10.5

print("FLOAT TO INT :", int(b))
print("FLOAT TO COMPLEX :", complex(b))
print("FLOAT TO STRING :", str(b))
print("FLOAT TO BOOLEAN :", bool(b))

# print(list(b))      # Error
# print(tuple(b))     # Error
# print(set(b))       # Error
# print(dict(b))      # Error

print()

# ==========================
# 3. complex Conversions
# ==========================
c = 3 + 4j

# print(int(c))       # Error
# print(float(c))     # Error

print("COMPLEX TO STRING :", str(c))
print("COMPLEX TO BOOLEAN :", bool(c))

print()

# ==========================
# 4. string Conversions
# ==========================
d = "123"

print("STRING TO INT :", int(d))
print("STRING TO FLOAT :", float(d))
print("STRING TO COMPLEX :", complex(d))
print("STRING TO LIST :", list(d))
print("STRING TO TUPLE :", tuple(d))
print("STRING TO SET :", set(d))
print("STRING TO BOOLEAN :", bool(d))

print()

# ==========================
# 5. list Conversions
# ==========================
e = [1, 2, 3]

print("LIST TO TUPLE :", tuple(e))
print("LIST TO SET :", set(e))
print("LIST TO STRING :", str(e))
print("LIST TO BOOLEAN :", bool(e))

# print(int(e))       # Error
# print(float(e))     # Error
# print(complex(e))   # Error
# print(dict(e))      # Error

print()

# ==========================
# 6. tuple Conversions
# ==========================
f = (1, 2, 3)

print("TUPLE TO LIST :", list(f))
print("TUPLE TO SET :", set(f))
print("TUPLE TO STRING :", str(f))
print("TUPLE TO BOOLEAN :", bool(f))

# print(int(f))       # Error

print()

# ==========================
# 7. set Conversions
# ==========================
g = {1, 2, 3}
 
print("SET TO LIST :", list(g))
print("SET TO TUPLE :", tuple(g))
print("SET TO STRING :", str(g))
print("SET TO BOOLEAN :", bool(g))

# print(int(g))       # Error
print()

# ==========================
# 8. dictionary Conversions
# ==========================
h = {"name": "Zaib", "age": 22}

print("DICT TO LIST :", list(h))
print("DICT TO TUPLE :", tuple(h))
print("DICT TO SET :", set(h))
print("DICT TO STRING :", str(h))
print("DICT TO BOOLEAN :", bool(h))

print()

# ==========================
# 9. boolean Conversions
# ==========================
i = True

print("BOOL TO INT :", int(i))
print("BOOL TO FLOAT :", float(i))
print("BOOL TO COMPLEX :", complex(i))
print("BOOL TO STRING :", str(i))

# print(list(i))      # Error
# print(tuple(i))     # Error
# print(set(i))       # Error
print(dict(i))      # Error


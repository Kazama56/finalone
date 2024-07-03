# Types of inheritance
# 1. Single
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance



# Single Inheritance
class A:
    a = 1

class B(A):
    b = 2

obj = B()
# print(obj.name)  # Attribute Error


# Multiple Inheritance
class A:
    a = 2

class B:
    b = 1


class C(A, B):  # Multiple Inheritance
    c = 3


# Multilevel Inheritance
class A:
    a = 1

class B(A):
    b = 3

class C(B):
    c = 12


# Hierarchical
class A:
    a = 1

class B(A):
    b = 3


class C(A):
    c = 2



# Hybrid Inheritance
# It is the combination of multiple and hierarchical inheritance

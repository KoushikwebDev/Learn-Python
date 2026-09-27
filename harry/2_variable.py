a = 1
print(a)

b = "harry"
print(b)


obj = {"a": "str"}
print(obj)


x = 2
y = 1
print(x + y)


# ? Find type of a vaiable

boolean = True
z = "Hello"
print(type(x), type(z), type(boolean))  # int, str, bool


complexNumber = complex(2, 3)  # 2+3j
print(complexNumber, type(complexNumber))  # "complex Number"

floatNumber = 1.1
print(type(floatNumber))  # float

v = None
print(type(v))  # NoneType

# #####
list1 = [1, 2.3, "Koushik", True]
print(type(list1))  # list

# ? List can be muatable

list1[0] = 6

list1 = "str"

print(list1)


# * tuple

tuple1 = ("parrot", 1, True, 1.1)
# tuple1[0] = "Hello"  #? cant do that immutable
print(tuple1[0])


# * Dictionary

map1 = {}


print(type(map1))  # dict

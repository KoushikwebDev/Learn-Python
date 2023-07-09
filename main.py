# name = "KSaha"
# # for x in name:
# #     print(x)


# a = "Hello"
# print(len(a))
# print(a[-2:-3])


# list1 = ["apple", "sum", "Orange"]

# # print(len(list1))
# # print(list1[0])

# i = len(list1)

# while i > 0:
#     # print(list1[i - 1])
#     if list1[i - 1].startswith("s"):
#         print(list1[i - 1])
#     i = i - 1


# # print(list1[0].startswith("s"))


for x in range(6):
    if x == 10:
        break
    print(x)
else:
    # print("Finally finished!")
    pass


def abc():
    print("Hello mousumi")
    print("abc")


# abc()
print(1 + 2)


def mousumi(a, b, c=45):
    print(a + b + c)


mousumi(23, 100, 10)
# mousumi(12, 34)

# mousumi(c=45, b=10, a=24)


print(type(mousumi))


def covertIntoCapitalize(string):
    # print(str.capitalize())

    return string.upper()


x = covertIntoCapitalize("mou pal")
print(x)


def add(x, y):
    # print(type(x))
    # if not isinstance(x, int):
    #     return "Please enter valid number"

    if type(x) != int or type(y) != int:
        return "Please enter a valid number"

    return x + y


print(add("hi", 34))
print(add(23, "gi"))


# print(isinstance(4, bool))
# print(type(4) == int)


import time

print(time.perf_counter())


demo, demo1 = "mou", "soytan"
print(demo, demo1)
print(type(demo))

str3 = "Hello\nKoushik\n"
print(str3)

print(6 / 3 * 2.0)
print(6 / (3 + -2))
print(6 / 3 + -2)
print(6 / (3 + -2))


str1 = "abcdef"

for char in str1:
    print(char.upper())

marks = [1, 2, 3, 4, "all marks", True]
print(marks)
print(type(marks))
print(len(marks))


print(marks[0])
print(marks[1])
print(marks[2])
# print(marks[7]) #error


print(marks[-2])  # length of list - 2 = 6 -2 = 4 => all marks


for ele in marks:
    # print(ele)
    pass


# ?

print(4 in marks)  # * True


print("kou" in "koushik")  # * True


# ? Slice
# marks = [1, 2, 3, 4, "all marks", True]


print(marks[:])  # * marks[0:len(marks)] => [1, 2, 3, 4, 'all marks', True]

print(marks[1:2])  # * [2]

print(marks[1:-1])  # * [  2, 3, 4, "all marks"]


# ? Jump Index

print(marks[1:-1:2])


# ? List comprehension 🚀🚀🚀

list1 = [i for i in range(10)]
print(list1)  # * [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


lst = [i * 2 for i in range(10)]
print(lst)  # * [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


list2 = ["kou", "Mou", "al", "jel", "mel", "fol", "jo", "hu"]

# ? copy list items
list3 = [ele for ele in list2]
print(list3)  # * ['kou', 'Mou', 'al', 'jel', 'mel', 'fol']

# ? copy list items which contains "o"
list4 = [ele for ele in list2 if "o" in ele]
print(list4)  # * ['kou', 'Mou', 'fol']

# ? copy list which element length greater than 2
list5 = [ele for ele in list2 if len(ele) > 2]
print(list5)  # * ['kou', 'Mou', 'jel', 'mel', 'fol']

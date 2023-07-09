marks = [1, 2, 3, 4, 23, 45, 100, 34, 224]

marks.append(10)

print(marks)  # * [1, 2, 3, 4, 23, 45, 100, 34, 224, 10]

marks.sort()  # ascending order
print(marks)  # * [1, 2, 3, 4, 10, 23, 34, 45, 100, 224]

marks.sort(reverse=True)  # decending order
print(marks)  # * [224, 100, 45, 34, 23, 10, 4, 3, 2, 1]


marks.reverse()  # it reverse array element
print(marks)  # * [1, 2, 3, 4, 10, 23, 34, 45, 100, 224]

# ? find index of an element
print(marks.index(100))  # *  8


# ? Copy a list

list1 = [1, 2, 3, 4, 5]

list2 = list1
list2[0] = 100
print(list1)  # * [100, 2, 3, 4, 5]


list3 = list1.copy()
list3[0] = 200
print(list1)  # * [100, 2, 3, 4, 5]
print(list3)  # * [200, 2, 3, 4, 5]


# ? insert to an index
list4 = [1, 2, 3]
list4.insert(0, 100)
print(list4)  # * [100, 1, 2, 3]

# ? extend a list

list5 = [1, 2, 3, 4]
list6 = [5, 6, 7, 8, 9]

list5.extend(list6)
print(list5)  # * [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ? concat list

list7 = [1, 2]
list8 = [3]
list9 = list7 + list8
print(list9)  # * [1, 2, 3]

nums = [1, 2, 3, 4]

result = map(lambda n: n * 2, nums)

print(list(result))
# [2, 4, 6, 8]
# Important: Python's map() returns a map object (iterator), so you commonly convert it to a list.


# alternative
nums = [1, 2, 3, 4]

result = [n * 2 for n in nums]
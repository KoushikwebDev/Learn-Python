nums = [1, 2, 3, 4, 5]

result = filter(lambda n: n > 2, nums)

print(list(result))
# [3, 4, 5]


# alternative
nums = [1, 2, 3, 4, 5]

result = [n for n in nums if n > 2]
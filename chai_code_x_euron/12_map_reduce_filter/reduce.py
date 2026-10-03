from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda total, n: total + n, nums, 0)

print(result)
# 10
nums = [-1, -2, -3, -4, 1, 2, 4]

def countPositiveNumber(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

print(countPositiveNumber(nums))
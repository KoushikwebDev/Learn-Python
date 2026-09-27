# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]


def isDuplicateExists():
    arr = []
    for item in items:
        if item in arr:
            return "Duplicate found"
        else:
            arr.append(item)

print(isDuplicateExists())
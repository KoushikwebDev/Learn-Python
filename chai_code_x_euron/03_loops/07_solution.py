def getValidNumber():
    num = int(input("Pls enter a number in between 0 to 10: "))
    if num > 0 and num <= 10:
        return "Passed"
    else :
        return getValidNumber()

print(getValidNumber())


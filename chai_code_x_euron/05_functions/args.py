
# arguments with *args => here args is a tuple
def sumOfn (*args):
    return sum(args) # sum is a built-in function that returns the sum of all the elements in the iterable


print(sumOfn(1,2,3,4,5,6)) # 21

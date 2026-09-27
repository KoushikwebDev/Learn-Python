# * Iterate String

name = "koushik"

for x in name:
    print(x)
    if x == "k":
        print("1st and last letter is k")


# * iterate list

colors = ["red", "orange", "blue", "Yellow", "green"]
for color in colors:
    print(color)
    for x in color:
        print(x)


# ? range

for k in range(100):
    print(k)  # * it prints 0 to 99
    print(k + 1)  # * it prints 1 to 100


for i in range(4, 10):
    print(i)  # * it prints 4 to 9


# * The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)


for i in range(2, 50, 3):
    print(i)


for x in range(6):
    if x == 10:
        break
    print(x)
else:
    print("Finally finished!")


# * pass

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass

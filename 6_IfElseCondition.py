age = int(input("Enter Your age "))

if age >= 18:
    print("You can drive now 🚀🚀🚀")
elif age <= 0:
    print("Enter valid age")
elif age <= 0:
    print("Age is less than and equal to 10")
else:
    print("not are not elegible 😒😒")


# ? Indentation starts a block in python


# ? Nested if else

num = -3

if num > 0:
    print("Num is positive number")
elif num < 0:
    print("Num is neagtive number")
    if num < 5:
        print("Num is less than 5")
else:
    print("Bag bsdk")


import time

str = time.strftime("%H:%M:%S")  # * => 22:06:55 => Current time
print(str)


# Good morning question

if int(time.strftime("%H")) == 00:
    print("Good Morning sir")

else:
    print("Good night sir")

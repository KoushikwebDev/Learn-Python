# age = int(input("Enter your age : "))

age = 22

def ageClassifier(age):
    if age <= 13:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

print(ageClassifier(age))

# ----------------------------------------


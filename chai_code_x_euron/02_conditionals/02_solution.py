age = 22
day = "Wednesday"


# price = 12 if age >= 18 else 8

def ticketPricing(age, day):
    price = 12 if age >= 18 else 8
    if day == "Wednesday":
        return price - 2
    else:
        return price

print(ticketPricing(age, day))
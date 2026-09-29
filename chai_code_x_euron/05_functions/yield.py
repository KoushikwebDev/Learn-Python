

def eventGenerator(limit):
    for i in range(2, limit, 2):
        print(f"Event : {i}")

# eventGenerator(10)  # Event : 2, Event : 4, Event : 6, Event : 8


def evenGenerator(limit):
    for i in range(2, limit, 2):
        yield i  # yield is used to return a generator object
        # print(f"Even : {i}")

# print(list(evenGenerator(10)))  # [2, 4, 6, 8]

for i in evenGenerator(10):
    print(f"Even : {i}")  # Even : 2, Even : 4, Even : 6, Even : 8
x = 3


match x:
    case 1:
        print("Not matched")
    case 0:
        print("Matched the value of X")
    case _ if x != 4:
        print("x not equal to 4")
    case _:
        print("Default value")

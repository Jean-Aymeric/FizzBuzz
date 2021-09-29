for i in range(1, 101):
    atLeastOneDivider = False
    if i % 3 == 0:
        print("Fizz", end="")
        atLeastOneDivider = True
    if i % 5 == 0:
        print("Buzz", end="")
        atLeastOneDivider = True
    if not atLeastOneDivider:
        print(i, end="")
    print("")

for i in range(1, 101):
    atLeastOneDivisor = False
    if i % 3 == 0:
        print("Fizz", end="")
        atLeastOneDivisor = True
    if i % 5 == 0:
        print("Buzz", end="")
        atLeastOneDivisor = True
    if not atLeastOneDivisor:
        print(i, end="")
    print("")

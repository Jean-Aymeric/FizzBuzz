                            # i est un entier
for i in range(1, 101):     # Pour i allant de 1 à 100 inclu
    if i % 15 == 0:         #   Si i % 15 = 0 Alors
        print("FizzBuzz")   #       Afficher("FizzBuzz")
    elif i % 3 == 0:        #   Sinon   Si i % 3 = 0 Alors
        print("Fizz")       #               Afficher("Fizz")
    elif i % 5 == 0:        #           Sinon   Si i % 5 = 0 Alors
        print("Buzz")       #                       Afficher("Buzz")
    else:                   #                   Sinon
        print(i)            #                       Afficher(i)
                            #                   FinSi
                            #           FinSi
                            #   FinSi
                            # FinPour

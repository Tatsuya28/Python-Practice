""" Générateur des nombres de la suite de Fibonacci

La série mathématique connue sous le nom de suite de Fibonacci a été l’une des questions informatique les plus populaires. Essentiellement, vous commencez avec deux nombres, de préférence 0 et 1, et vous les ajoutez pour créer votre troisième nombre de Fibonacci. Ensuite, il suffit d’additionner la somme et l’avant-dernier terme de Fibonacci pour générer le suivant.

Exemple : n = 42
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141
 """

import os
import sys

CLEAR = "cls" if sys.platform == "win32" else "clear"


def fibonacci(laps, id, a, b):
    if id == laps:
        print(a)
        return
    else:
        print(a, end=' ')
        return fibonacci(laps, id + 1, b, a + b)


os.system(CLEAR)
n = int(input("Please select the n-th number of the fibonacci sequence : "))
print("Here, the values until the {0}-th fibonacci term : ".format(n))
fibonacci(n, 1, 1, 1)

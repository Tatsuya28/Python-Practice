""" Le juste prix

Ce premier projet est un jeu amusant pour les débutants connu de tous. Le programme génère un prix rond aléatoire. Le but pour l’utilisateur est de deviner le prix. Chaque fois que l’utilisateur se trompe, l’ordinateur lui dit si c’est plus ou moins que le prix qu’il a donné. À chaque aide de l’ordinateur, le score final atteignable par le joueur baisse.

Au programme, vous apprendrez à saisir des entrées clavier par un utilisateur, créer des fonctions pour valider que le nombre entré est bien un nombre entier, comparer une variable de référence (le prix) avec une autre variable et de calculer la différence entre deux nombre. """


from random import randint


guess = randint(0, 1000)
found = False
number = 0
nb_try = 0

print("\n\nWe will play to Guess the Price.\nFor that, a random number between 0 and 1000 has been drawn. Try to guess it!")

while not found:
    number = input("Your assumption: ")
    while not number.isdigit():
        number = input("Please enter a number! Your assumption: ")
    number = int(number)
    nb_try += 1

    if number == guess:
        print(f"Congratulations you found it in {nb_try} try!")
        found = True
    elif number < guess:
        print("It's more!")
    elif number > guess:
        print("It's less!")
    else:
        print("Error")
        break

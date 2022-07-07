""" Le juste prix avec la recherche dichotomique """

from random import randint

#

found = False
number = 0
nb_try = 0
inf_bound = 0
sup_bound = 100000
guess = randint(inf_bound, sup_bound)

print(f"\n\nWe will play to Guess the Price.\nFor that, a random number between {inf_bound} and {sup_bound} has been drawn. Try to guess it!")

while (found == False):
    nb_try += 1
    
    number = inf_bound + (sup_bound - inf_bound) // 2

    print(f"Assumption : {number}")

    if number == guess:
        print("Congratulations you found it in " + str(nb_try) + " try! \n")
        found = True
    elif number < guess:
        print("It's more!\n")
        inf_bound = number
    elif number > guess:
        print("It's less!\n")
        sup_bound = number
    else:
        print("Error")
        break
    input("Press enter to continue...")
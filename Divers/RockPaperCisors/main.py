""" Pierre Papier Ciseaux

Créer un pierre papier ciseaux est un bon exercice pour vous entraîner en Python et réaliser vos premiers projets.

Au programme, vous devrez créer :

    une fonction qui génère de l’aléatoire : pierre, papier ou ciseaux
    une fonction pour vérifier et valider le coup qui vient d’être joué
    ---une fonction de résultat pour déclarer le vainqueur du tour---
    un compteur de points pour suivre le score total

Le programme demande à l’utilisateur d’effectuer le premier coup avant d’effectuer un coup. Une fois le coup validé, l’entrée est évaluée, l’entrée saisie pouvant être une chaîne de caractères, une lettre ou un nombre. Après évaluation de la chaîne de caractères, la fonction de résultat détermine le gagnant et la fonction de comptabilisation des points actualise le score total. """

import os
import sys
from random import choice

CLEAR = "cls" if sys.platform == "win32" else "clear"

ROCK = 0b001
PAPER = 0b010
SCISSORS = 0b100

winner = {ROCK | PAPER: PAPER, PAPER | SCISSORS: SCISSORS, SCISSORS | ROCK: ROCK, ROCK: None, PAPER: None,
          SCISSORS: None}

score = {"player": 0, "ai": 0}


def random_move():
    return choice([ROCK, PAPER, SCISSORS])


def int_input(message, predicate, stderr=''):
    val = None
    while not val:
        val = input(message)
        if not val.isdigit() or not predicate(int(val)):
            print("Error, please correct your input!\n" + stderr)
        else:
            val = int(val)
    return val


turns = None
while not turns:
    turns = int_input("How many turns do you want to do?\nYou >", lambda x: x > 0, stderr="This is not a number!")

for turn in range(turns):
    os.system(CLEAR)
    print(f"Remaining turns : {turns - turn - 1}")
    print("What do you want to play?\n1. Rock\n2. Paper\n3. Scissors\n")

    player_move = None
    while not player_move or player_move not in [1, 2, 3]:
        player_move = int_input("You >", lambda x: x in (1, 2, 3))
    player_move = [ROCK, PAPER, SCISSORS][player_move - 1]
    ai_move = random_move()

    print(
        f"You: { {ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors'}[player_move]}!\tVS\tComputer: { {ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors'}[ai_move]}!")

    if player_move == winner[player_move | ai_move]:
        print("You win!")
        score["player"] += 1
    elif ai_move == winner[player_move | ai_move]:
        print("You lose!")
        score["ai"] += 1
    else:
        print("Tie!")

    input("Press enter to continue...")

print("{:^20}".format("---- SCORES ----"))
print("{:<10}:{:>10}".format("Player", score['player']))
print("{:<10}:{:>10}".format("Computer", score['ai']))

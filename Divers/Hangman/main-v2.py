import os
import random

mots = {
    1: "GIRAFE",
    2: "MAISON",
    3: "CANAPE",
    4: "ORDINATEUR",
    5: "LEOPARD",
    6: "VAUTOUR",
    7: "OTARIE",
    8: "NOURRITURE",
    9: "FENETRE"
}

vies = 6
choix = random.randint(1, 9)
tentatives = ""
existe = False

affichage = "_ " * len(mots[choix])
lettres_trouvees = ""

while vies > 0:
    os.system("cls")
    print(f"Le mot à deviner est : {affichage}")
    lettre = input("\n> Devinez une lettre : ")[:1].upper()
    if not lettre.isalpha():
        print("Erreur de siaise, entrer une lettre !")
        input("Appuyez sur ENTRER pour continuer...")
        continue

    if lettre in tentatives:
        print("Vous avez déjà essayé cette lettre !")
        input("Appuyez sur ENTRER pour continuer...")
        continue
    tentatives += f"{lettre}, "

    if lettre in mots[choix]:
        lettres_trouvees += lettre
        print("-> Bien vu !")
    else:
        vies -= 1
        print("-> Raté !")
        print(f"Il vous reste {vies} vies !")

    affichage = "".join(f"{id} " if id in lettres_trouvees else "_ " for id in mots[choix])

    if "_" not in affichage:
        print(">>>  Gagné !  <<<")
        break

    input("Appuyez sur ENTRER pour continuer...")

if vies > 0:
    print(f"Vous avez trouvé le mot {mots[choix]}")
else:
    print(f">>> Perdu ! <<<\nLe mot à deviner était {mots[choix]} !")
print("  * FIN DE LA PARTIE *  ")

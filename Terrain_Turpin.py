################################################
# Groupe BI 2
# Lenny BACKORY
# Andrew BAYISSA
# Joris ANGAMAN
# Martin DIAMANT
# Amel LASSAL
# Thomas TURPIN
# https://github.com/uvsq22004392/projet_terrain
################################################

# Importation des libraires #

import tkinter as tk
import random as rd

# Définition des constantes #

LARGEUR, HAUTEUR = 500, 500
TAILLE_CASE = 10

# Définition des variables globales #

cases = []

T = 5
p = 50
n = 4
k = 1

racine = tk.Tk()

canvas = tk.Canvas(racine, height=LARGEUR, width=LARGEUR//2, bg="white")
canvas.grid(column=0)
canvas2 = tk.Canvas(racine, height=LARGEUR, width=HAUTEUR, bg="white")
canvas2.grid(column=1, row=0)

# Définition des fonctions #


def proba_eau():
    """Gère la probabilité du type de case initial."""
    feu = rd.randint(0, 100)
    if feu < p:
        return ["eau"]
    else:
        return ["terre"]


def couleur(lieu):
    """Retourne la couleur en fonction de la case."""
    if lieu == "terre":
        return "#157120"
    if lieu == "prairie":
        return "#1DE034"
    if lieu == "eau":
        return "#1D87E0"


def refresh():
    """Redessine le terrain."""
    for i in range(HAUTEUR // TAILLE_CASE):
        for j in range(LARGEUR // TAILLE_CASE):
            canvas2.create_rectangle(
                                    (i * TAILLE_CASE, j * TAILLE_CASE),
                                    (i * TAILLE_CASE + TAILLE_CASE,
                                     j * TAILLE_CASE + TAILLE_CASE),
                                    fill=couleur(cases[i][j][0]),
                                    width=0)


def moore(i, j):
    """Vérifie le nombre de voisins."""
    global cases
    MOORE = 0
    for a in range(-k, k + 1):
        for b in range(-k, k + 1):
            # Evite d'aller out of range
            if (i + a) <= 0 or (i + a) >= len(cases):
                pass
            elif (j + b) <= 0 or (j + b) >= len(cases[i]):
                pass
            elif cases[i + a][j + b] == ["eau"]:
                MOORE += 1
    return MOORE


def automate():
    """Vérifie le nombre de voisins avec moore(i, j) de toutes les cases."""
    global cases
    cases_tempo = [[[] for i in range(LARGEUR // TAILLE_CASE)]
                   for i in range(HAUTEUR // TAILLE_CASE)]
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            if moore(i, j) >= T:
                cases_tempo[i][j] = ["eau"]
            else:
                cases_tempo[i][j] = ["terre"]
    cases = list(cases_tempo)
    refresh()  # Ici et pas dans generer_terrain pour pouvoir tester


def generer_terrain():
    """Fonctions proba_eau() puis automate() puis refresh()."""
    global cases
    cases = []
    cases = [[proba_eau() for i in range(LARGEUR // TAILLE_CASE)]
             for i in range(HAUTEUR // TAILLE_CASE)]
    automate()


def taille_grille():
    pass


def creation_personnage():
    pass


def deplacement():
    pass


def sauvegarde_terrain():
    """Permet de sauvegarder le terrain dans un txt."""
    fic = open("sauvegarde.txt", "w")
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            if cases[i][j] == ["eau"]:
                fic.write("0")
            elif cases[i][j] == ["terre"]:
                fic.write("1")
        fic.write("/")
    fic.close()


def charger_terrain():
    """Charge un terrain depuis le txt."""
    global cases
    cases = []
    sous_liste = []
    fic = open("sauvegarde.txt", "r")
    lignes = fic.readline()
    for i in range(len(lignes)):
        if lignes[i] == "0":
            sous_liste.append(["eau"])
        elif lignes[i] == "1":
            sous_liste.append(["terre"])
        else:
            cases.append(sous_liste)
            sous_liste = []
    fic.close()
    refresh()


# Programme principal #

bouton1 = tk.Button(racine, text="Génération de terrain aléatoire",
                    font=("helvetica", "10"), command=generer_terrain)
bouton1.place(x=0, y=100)

bouton2 = tk.Button(racine, text="Sauvegarde du terrain",
                    font=("helvetica", "10"), command=sauvegarde_terrain)
bouton2.place(x=0, y=130)

bouton3 = tk.Button(racine, text="Charger un terrain",
                    font=("helvetica", "10"), command=charger_terrain)
bouton3.place(x=0, y=160)

bouton4 = tk.Button(racine, text="Automate (Moore)",
                    font=("helvetica", "10"), command=automate)
bouton4.place(x=0, y=190)

racine.mainloop()

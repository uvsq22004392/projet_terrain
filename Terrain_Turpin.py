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


# Définition des constantes

LARGEUR, HAUTEUR = 500, 500


# Définition des variables globales #

TAILLE_CASE = 10
cases = []
terrain = []

# Valeurs par défaut

T = 5  # Nombre de voisins conversion eau
p = 50  # Probabilité qu'une case soit de l'eau
n = 4  # Nombre d'applications de l'automate
k = 1  # Taille voisinage pour Moore
nbr_h = 50
nbr_l = 50
choix = False  # Apparaît dans generer_terrain

# Personnage

personnage = []  # Coordonnées du personnage
ancien_emplacement_personnage = []

# tkinter

racine = tk.Tk()
canvas = tk.Canvas(racine, height=550, width=250, bg="white")
canvas.grid(column=0)
canvas2 = tk.Canvas(racine, height=LARGEUR, width=HAUTEUR, bg="white")
canvas2.grid(column=1, row=0)


# Définition des fonctions #


def proba_eau():
    """Gère la probabilité du type de case initial."""
    feu = rd.randint(0, 100)  # Génère un nombre aléatoire
    if feu < p:  # Compare ce nombre p -> gère la probabilité
        return ["eau"]
    else:
        return ["terre"]


def couleur(lieu):
    """Retourne la couleur en fonction de la case."""
    if lieu == "terre":
        return "#157120"  # Vert
    if lieu == "eau":
        return "#1D87E0"  # Bleu


def refresh_personnage():
    """Créer un personnage en unicode"""
    global personnage
    global pk
    if personnage != []:  # Si il y a un personnage
        a = personnage[0]  # coordonnées x du curseur
        b = personnage[1]  # coordonnées y du curseur
        pk = canvas2.create_text( (a*TAILLE_CASE+6, b*TAILLE_CASE),text="\U0001F47D", fill= "red", font="MSGothic "+str(TAILLE_CASE-1))
        

def refresh():
    """Redessine le terrain."""
    global terrain
    for i in range(len(terrain)):
        canvas2.delete(terrain[-1])
        del terrain[-1]
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            terrain.append(canvas2.create_rectangle(
                                   (i * TAILLE_CASE, j * TAILLE_CASE),
                                   (i * TAILLE_CASE + TAILLE_CASE,
                                    j * TAILLE_CASE + TAILLE_CASE),
                                   fill=couleur(cases[i][j][0]),
                                   width=0))
    refresh_personnage()


def moore(i, j):
    """Vérifie le nombre de voisins."""
    global cases
    if cases[i][j] == ["eau"]:
        MOORE = - 1  # Permet d'éviter de compter la case en elle-même
    else:
        MOORE = 0
    # range(-k, k + 1) permet d'aller chercher tous les voisins
    # à k cases de distance
    # Exemple : k = 1 -> va chercher les cases de i - 1 à i + 1
    for a in range(-k, k + 1):
        for b in range(-k, k + 1):
            if (i + a) <= 0 or (i + a) >= len(cases):
                # Permet d'éviter de sortir de la liste
                pass
            elif (j + b) <= 0 or (j + b) >= len(cases[i]):
                # Permet aussi d'éviter de sortir de la liste
                pass
            elif cases[i + a][j + b] == ["eau"]:
                # Compte le nombre de cases d'eau
                MOORE += 1
    return MOORE


def automate():
    """Vérifie le nombre de voisins avec moore(i, j) de toutes les cases."""
    global cases
    cases_tempo = [[[] for i in range(LARGEUR // (LARGEUR // nbr_l))]
                   for i in range(HAUTEUR // TAILLE_CASE)]
    # cases_tempo est une liste temporaire que l'on modifie
    # pour ne pas prendre en compte nos modifications
    # pendant qu'on les effectue
    for repetition in range(n):  # On applique n fois l'automate
        for i in range(len(cases)):
            for j in range(len(cases[i])):
                if moore(i, j) >= T:  # On applique Moore
                    cases_tempo[i][j] = ["eau"]
                else:
                    cases_tempo[i][j] = ["terre"]
    cases = list(cases_tempo)  # On remplace cases par notre nouvelle liste
    refresh()  # Ici et pas dans generer_terrain pour pouvoir tester


def valeurs_par_defaut():
    """Rétablie les valeurs de terrain par défaut."""
    global T
    global p
    global n
    global k
    global nbr_h
    global nbr_l
    T = 5
    p = 50
    n = 4
    k = 1
    nbr_h = 50
    nbr_l = 50


def generer_terrain():
    """Fonctions proba_eau() puis automate() puis refresh()."""
    global cases
    global personnage
    global LARGEUR
    global HAUTEUR
    global TAILLE_CASE
    if choix:  # On récupère les dimensions choisies.
        appliquer_choix()
    else:  # On rétablie les valeurs par défaut au cas où
        # elles aient été modifiées au préalable.
        valeurs_par_defaut()
    TAILLE_CASE = HAUTEUR // nbr_h  # Calcule la taille des cases
    # NB : les cases seront toujours carrés, en fonction de la hauteur.
    canvas2.config(height=LARGEUR, width=HAUTEUR)
    # On réinitialise personnage et cases
    personnage = []
    cases = []
    cases = [[proba_eau() for i in range(LARGEUR // (LARGEUR // nbr_l))]
             for i in range(HAUTEUR // TAILLE_CASE)]
    # On fait proba_eau pour toutes les cases puis automate.
    automate()


def creation_personnage(event):
    """Affiche le personnage aux coordonnées du curseur."""
    global personnage
    x, y = event.x // TAILLE_CASE, event.y // TAILLE_CASE
    # Permet d'avoir des coordonnées entières
    # Donc un numéro de case
    if cases != [] and cases[x][y] == ['terre'] and personnage == []:
        # Ne marche que si il y a un terrain
        # Et que l'on clique sur de la terre
        # Et qu'il n'y a pas déjà un personnage
        personnage = [x, y]
        refresh_personnage()  # Permet d'afficher le personnage


def effacer(event):
    """Retire et replace le personnage"""
    # Retire le personnage quand on clique dessus avec double click
    global personnage
    personnage = []
    canvas2.delete(pk)
    refresh_personnage()


def deplacement(event):
    """Déplace le personnage en fonction de la flèche appuyée."""
    global personnage
    global pk
    global ancien_emplacement_personnage
    direction = event.keysym  # Récupère la touche appuyée
    i, j = personnage[0], personnage[1]
    ancien_emplacement_personnage.append([i, j])  # Retiens les déplacements
    if direction == "Up":
        j += -1
        if j < 0:  # Evite d'aller out of range
            j += 1
    elif direction == "Down":
        j += 1
        if j >= LARGEUR // (LARGEUR // nbr_l) or j >= HAUTEUR // TAILLE_CASE:
            j += -1
    elif direction == "Left":
        i += -1
        if i < 0:
            i += 1
    elif direction == "Right":
        i += 1
        if i >= HAUTEUR // TAILLE_CASE:
            i += -1
    if cases[i][j] == ["terre"]:
        # Ne se déplace pas sur l'eau
        personnage[0], personnage[1] = i, j
    canvas2.delete(pk)
    refresh_personnage()


def annuler_deplacement():
    """Utilise ancien_emplacement_personnage pour annuler un déplacement."""
    global personnage
    global ancien_emplacement_personnage
    if ancien_emplacement_personnage == []:  # Empêche les erreurs
        pass
    else:
        personnage[0] = ancien_emplacement_personnage[-1][0]
        personnage[1] = ancien_emplacement_personnage[-1][1]
        del ancien_emplacement_personnage[-1]
    canvas2.delete(pk)
    refresh_personnage()


def sauvegarde_terrain():
    """Permet de sauvegarder le terrain dans un txt. cases est écrit sur
       la première ligne, personnage sur la seconde."""
    fic = open("sauvegarde.txt", "w")
    # On ouvre le fichier de sauvegarde en écriture
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            if cases[i][j] == ["eau"]:
                fic.write("0")  # On écrit 0 pour les cases d'eau
            elif cases[i][j] == ["terre"]:
                fic.write("1")  # On écrit 1 pour les cases de terre
        fic.write("/")  # On écrit / pour signifier la fin d'une ligne
    fic.write("\n")  # Va à la ligne
    fic.write(str(personnage[0]))  # Sauvegarde le personnage
    fic.write("\n")
    fic.write(str(personnage[1]))  # Sauvegarde le personnage
    fic.close()  # On ferme le fichier (IMPORTANT)


def charger_terrain():
    """Charge un terrain depuis le txt."""
    global cases
    global personnage
    cases = []  # On vide le terrain actuel
    sous_liste = []  # Sous-liste que l'on placera dans cases
    fic = open("sauvegarde.txt", "r")
    # On ouvre le fichier de sauvegarde en lecture
    lignes = fic.readline()  # Lis une ligne
    for i in range(len(lignes)):
        if lignes[i] == "0":
            sous_liste.append(["eau"])
        elif lignes[i] == "1":
            sous_liste.append(["terre"])
        else:
            cases.append(sous_liste)
            sous_liste = []
    # On ajoute les cases à une sous-liste que l'on place dans
    # la liste cases, puis on efface la sous-liste quand on voit /
    # et on recommance.
    # Lis la deuxième ligne
    personnage = []
    personnage.append(int(fic.readline()))
    personnage.append(int(fic.readline()))
    fic.close()  # Bien penser à fermer le fichier !
    refresh()  # On actualise pour pouvoir voir le résultat.


def appliquer_choix():
    """Applique les paramètres choisis par l'utilisateur."""
    global p
    global n
    global T
    global k
    global nbr_h
    global nbr_l
    global choix
    global Frame
    p = int(choixp.get())
    n = int(choixn.get())
    T = int(choixT.get())
    k = int(choixk.get())
    nbr_h = int(entree2.get())
    nbr_l = int(entree1.get())
    choix = False
    Frame.destroy()
    canvas2.focus_set()  # Permet d'utiliser le clavier sur le canvas


def fenetre_choix():
    """Affiche une fenêtre permettant à l'utilisateur
       de paramétrer la génération de terrain."""
    global entree1
    global entree2
    global choixp
    global choixk
    global choixT
    global choixn
    global Frame
    global choix

    Frame = tk.Frame(racine, height=0, width=0)
    Frame.grid(column=3, row=0)
    Frame.config(height=500, width=250)

    entree1 = tk.Entry(Frame)
    entree1.place(x=0, y=25)
    entree1.insert(0, 50)  # Valeur par défaut

    texte1 = tk.Label(Frame, text="Entrez le nombre de cases en largeur")
    texte1.place(x=0, y=5)

    entree2 = tk.Entry(Frame)
    entree2.place(x=0, y=70)
    entree2.insert(0, 50)  # Valeur par défaut

    texte2 = tk.Label(Frame, text="Entrez le nombre de cases en hauteur")
    texte2.place(x=0, y=50)

    choixp = tk.Entry(Frame)
    choixp.place(x=0, y=120)
    choixp.insert(0, 50)  # Valeur par défaut

    texte3 = tk.Label(Frame, text="Entree la valeur de p (en %)")
    texte3.place(x=0, y=100)

    choixn = tk.Entry(Frame)
    choixn.place(x=0, y=165)
    choixn.insert(0, 4)  # Valeur par défaut

    texte4 = tk.Label(Frame, text="Entree la valeur de n")
    texte4.place(x=0, y=140)

    choixT = tk.Entry(Frame)
    choixT.place(x=0, y=230)
    choixT.insert(0, 5)  # Valeur par défaut

    texte5 = tk.Label(Frame, text="Entree la valeur de T")
    texte5.place(x=0, y=200)

    choixk = tk.Entry(Frame)
    choixk.place(x=0, y=285)
    choixk.insert(0, 1)  # Valeur par défaut

    texte4 = tk.Label(Frame, text="Entree la valeur de k")
    texte4.place(x=0, y=260)

    bouton_generation = tk.Button(Frame, text="Generer le terrain",
                                  command=generer_terrain)
    bouton_generation.place(x=100, y=350)

    choix = True


# Programme principal #

bouton0 = tk.Button(racine, text="Génération de terrain aléatoire par défaut",
                    font=("helvetica", "10"), command=generer_terrain)
bouton0.place(x=0, y=70)


bouton1 = tk.Button(racine, text="Modifier les paramètres de la génération",
                    font=("helvetica", "10"), command=fenetre_choix)
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

bouton5 = tk.Button(racine, text="Annuler déplacement",
                    font=("helvetica", "10"), command=annuler_deplacement)
bouton5.place(x=0, y=220)


# Liaison des evenements

canvas2.bind("<Button-1>", creation_personnage)
canvas2.focus_set()  # Permet d'utiliser le clavier sur le canvas
canvas2.bind("<Key>", deplacement)
canvas2.bind("<Double-Button-1>", effacer)


racine.mainloop()

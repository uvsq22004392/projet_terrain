import tkinter as tk
import random as rd

# Définition des constantes #

LARGEUR, HAUTEUR = 500, 500
TAILLE_CASE = 20

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
    #Bon là la fonction est pas très utile je verrai ce qu'on en fait plus tard
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


def generer_terrain_initial():
    """Fonctions proba_eau() puis refresh()."""
    #à compléter par la suite
    global cases
    cases = []
    cases = [[proba_eau() for i in range(LARGEUR // TAILLE_CASE)]
             for i in range(HAUTEUR // TAILLE_CASE)]
    refresh()

def moore (i, j):
    pass


def automate ():
    pass


def taille_grille():
    pass

#################################################################
### Fonctions création du personnage et déplacement

CHARACTER = False
def personnage(event):
    """Créer un personnage en Unicode dans un point donnée lors d'un clic gauche de la souris"""
    global CHARACTER
    if CHARACTER:
        return
    else:
        i=event.x
        j=event.y
        print("clic aux coordonnées event  ", event.x , event.y)
        print("clic aux coordonnées i et j ", i , j)
        #canvas.create_text(int(j/20),int(i/20), text = "👽")
        personnage = tk.Label(racine, text="👽")
        personnage.place( x=i,y=j) #x=(i%20)*20,y=(j%20)*20
        CHARACTER = True



def deplacement():
    if lieu == "terre":
        personnage[0]
        personnage[1]


#########################################################################

def sauvegarde_terrain():
    pass

def charger_terrain():
    pass



#def etape_suivante():
#    """Gère le déroulement de la simulation."""
#    global cases
#    for i in range(1, HAUTEUR // TAILLE_CASE - 1):
#        for j in range(1, LARGEUR // TAILLE_CASE - 1):
#            if cases[i][j][0] == 'foret':
#                nf = 0
#                if cases[i-1][j][0] == 'feu':
#                    nf += 1
#                if cases[i+1][j][0] == 'feu':
#                    nf += 1
#                if cases[i][j+1][0] == 'feu':
#                    nf += 1
#                if cases[i-1][j-1][0] == 'feu':
#                    nf += 1
#                if etat_foret(nf) == "feu":
#                    cases[i][j] = ["feu", DUREE_FEU]
#            elif cases[i][j][0] == 'prairie':
#                if cases[i-1][j][0] == 'feu' or cases[i+1][j][0] == 'feu' \
#                        or cases[i][j+1][0] == 'feu' \
#                        or cases[i][j-1][0] == 'feu' \
#                        or cases[i-1][j][0] == 'feu' \
#                        or cases[i+1][j][0] == 'feu':
#                    cases[i][j] = ["feu", DUREE_FEU]
#            if cases[i][j][0] == "feu":
#                cases[i][j][1] += -1
#                if cases[i][j][1] <= 0:
#                    cases[i][j][0], cases[i][j][1] = "cendres", DUREE_CENDRES
#            elif cases[i][j][0] == "cendres":
#                cases[i][j][1] += -1
#                if cases[i][j][1] <= 0:
#                    cases[i][j] = ["cendres_eteintes"]
#
#    refresh()


# Programme principal #

# Liaison des évenements
canvas.bind("<Button-1>", personnage)

#Bon là tout ça faudra changer mais là j'ai eu la flemme
bouton1 = tk.Button(racine, text="Génération de terrain aléatoire",
                    font=("helvetica", "10"), command=generer_terrain_initial)
bouton1.place(x=0, y=100)

bouton2 = tk.Button(racine, text="Sauvegarde du terrain",
                    font=("helvetica", "10"))
bouton2.place(x=0, y=130)

bouton3 = tk.Button(racine, text="Charger un terrain",
                    font=("helvetica", "10"))
bouton3.place(x=0, y=160)

#bouton4 = tk.Button(racine, text="Prochaine étape",
                    #font=("helvetica", "10"), command=etape_suivante)
#bouton4.place(x=0, y=200)

bouton5 = tk.Button(racine, text="Démarrer la simulation",
                    font=("helvetica", "10"))
bouton5.place(x=0, y=230)

bouton6 = tk.Button(racine, text="Stopper la simulation",
                    font=("helvetica", "10"))
bouton6.place(x=0, y=260)

racine.mainloop()
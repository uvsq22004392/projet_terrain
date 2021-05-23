# projet_terrain

Ce programme génère un terrain de jeu de façon procédurale, et vous permez d'y placer et déplacer un personnage.
Lors de l'exécution, une fenêtre comportant plusieurs boutons va s'ouvrir.

Le bouton "Génération de terrain aléatoire par défaut" permet, comme son nom l'indique, de générer le terrain avec les paramètres par défaut.
Le bouton "Modifier les paramètres de la génération" ouvre un nouvel onglet qui permet de modifier les paramètres de la génération. Vous pouvez alors :
  - Modifier les dimensions du terrain (Notez que la fenêtre qui affiche le terrain conservera toujours les mêmes dimensions, à savoir 500 par 500 pixels, et que la taille des cases dépend de la hauteur du terrain.)
  -  Modifier la valeur de p (Pourcentage de chance pour lequel une case sera de l'eau)
  -  Modifier la valeur de n (Nombre d'applications de l'automate de génération)
  -  Modifier la valeur de T (Nombre de cases voisines d'eau à partir duquel une case sera convertie en case d'eau)
  -  Modifier la valeur de k (Taille du voisinage, en cases)
 
Les boutons "Sauvegarde du terrain" et "Charger un terrain" servent respectivement à sauvegarder et à charger un terrain vers et depuis le fhicher "sauvegarde.txt".

Le bouton "Automate (Moore)" permet d'appliquer l'automate de génération de terrain une fois.
Enfin, le bouton "Annuler déplacement" permet d'annuler le déplacement du personnage.


Lorsque le terrain a été généré, vous pouvez cliquer sur une case de terre (les cases vertes) afin d'y placer un personnage (symbolisé par un carré rouge).
Vous pouvez alors déplacer le-dit personnage grâce aux flèches de direction de votre clavier. Gardez en tête le fait que vous ne pouvez pas vous rendre sur les cases d'eau.

Si vous retirer votre personnage du jeu, vous pouvez faire un double-clic gauche sur le terrain, qui supprimera votre personnage.

# Crédits : 
- Martin DIAMANT (chef de projet et responsable de la relecture flake8)
- Lenny BACKORY (gestionnaire du dépôt GitHub)
- Andrew BAYISSA
- Amel LASSAL
- Thomas TURPIN

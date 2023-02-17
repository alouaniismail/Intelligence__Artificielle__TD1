import copy
import math

#fonction qui affiche la grille du jeu(morpion 3*3)

def afficher_grille(grille):
    for i in range(3):
        for j in range(3):
            print(grille[i][j],end=" ") #end<=>l'espaçage entre deux cases
        print() #saut de la ligne

#fonction qui vérifie si un joueur a gagné

def verifier_gagnant(grille, joueur):
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == joueur:
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] == joueur:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False #vérifie si un morpion est une instance gagnante

#fonction qui retourne les coups validés pour un joueur

def coups_valides(grille):
    coups = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                coups.append((i, j))
    return coups #tous les coups possibles en (i,j) qu'on peut marquer.

# Fonction qui calcule le score de la grille pour un joueur

def evaluer(grille, joueur):
    if verifier_gagnant(grille, joueur):#1 si joueur gagne
        return 1
    elif verifier_gagnant(grille, autre_joueur(joueur)):#-1 si l'autre ('O') 
        return -1
    else:
        return 0 #cas contraire
    
# Fonction qui retourne l'autre joueur

def autre_joueur(joueur):
    if joueur == "X":
        return "O"
    else:
        return "X"

# Fonction qui renvoie le meilleur score et le meilleur coup pour un joueur donné
def minimax(grille, joueur):
    if verifier_gagnant(grille, "X"):
        return (-1, None)
    elif verifier_gagnant(grille, "O"):
        return (1, None)
    elif verifier_match_nul(grille):
        return (0, None)

    if joueur == "O":
        meilleur_score = -math.inf
        signe = 1
    else:
        meilleur_score = math.inf
        signe = -1

    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                grille[i][j] = joueur
                score = signe * minimax(grille, "O" if joueur == "X" else "X")[0]
                grille[i][j] = "-"
                if score * signe > meilleur_score * signe:
                    meilleur_coup = (i, j)
                    meilleur_score = score
    return (meilleur_score, meilleur_coup)

# Fonction qui vérifie si la grille est remplie sans gagnant
def verifier_match_nul(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "-":
                return False
    return True


# Fonction qui permet à l'humain de jouer contre l'IA
def jouer():
    grille = [["-" for j in range(3)] for i in range(3)]
    tour = "X"
    while True:
        afficher_grille(grille)
        if tour == "X":
            ligne = int(input("Entrez la ligne : "))
            colonne = int(input("Entrez la colonne : "))
            if grille[ligne][colonne] != "-":
                print("Case déjà occupée. Réessayez.")
                continue
            grille[ligne][colonne] = tour
            if verifier_gagnant(grille, tour):
                afficher_grille(grille)
                print("Le joueur", tour, "a gagné !")
                break
            if verifier_match_nul(grille):
                afficher_grille(grille)
                print("Match nul !")
                break
            tour = "O"
        else:
            print("Tour de l'IA (O)...")
            coup = minimax(grille, "O")[1]
            grille[coup[0]][coup[1]] = "O"
            if verifier_gagnant(grille, tour):
                afficher_grille(grille)
                print("Le joueur", tour, "a gagné !")
                break
            if verifier_match_nul(grille):
                afficher_grille(grille)
                print("Match nul !")
                break
            tour = "X"

if __name__!='main':
    jouer()
    

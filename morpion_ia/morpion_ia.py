import math

HUMAIN='X'
IA='O' #l'ia joue en 'O'

def dessiner_plateau(plateau): #on dessine le plateau normalement
    print(plateau[0] + '|' plateau[1] + '|' + plateau[2])
    print('-+-+-+')
    print(plateau[3] + '|' plateau[4] + '|' + plateau[5])
    print('-+-+-+')
    print(plateau[6] + '|' plateau[7] + '|' + plateau[8])

def verifier_victoire(plateau,symbole):#on vérifie si on a gagné
    return ((plateau[0] == symbole and plateau[1] == symbole and plateau[2] == symbole) or
            (plateau[3] == symbole and plateau[4] == symbole and plateau[5] == symbole) or
            (plateau[6] == symbole and plateau[7] == symbole and plateau[8] == symbole) or
            (plateau[0] == symbole and plateau[3] == symbole and plateau[6] == symbole) or
            (plateau[1] == symbole and plateau[4] == symbole and plateau[7] == symbole) or
            (plateau[2] == symbole and plateau[5] == symbole and plateau[8] == symbole) or
            (plateau[0] == symbole and plateau[4] == symbole and plateau[8] == symbole) or
            (plateau[2] == symbole and plateau[4] == symbole and plateau[6] == symbole))


def verifier_match_nul(plateau):#on vérifie si le match joué est nul
    return all([case != ' ' for case in plateau])

def obtenir_cases_vides(plateau):#on récupère les cases vides à l'instant
    #dans le plateau
    return [i for i, case in enumerate(plateau) if case == ' ']

def coup_gagnant(plateau,symbole):#on vérifie s'il existe un coup gagnant
    #dans l'instance de ce plateau et on retourne le coup correspondant
    for coup in obtenir_cases_vides(plateau):
        copie_plateau=plateau.copie()
        copie_plateau[coup]=symbole
        if verifier_victoire(copie_plateau,symbole):
            return coup
        return None

def minmax(plateau,profondeur,maximisant_joueur):
    if verifier_victoire(plateau,IA):
        return (None,100-profondeur)
    elif verifier_victoire(plateau,HUMAIN):
        return (None,-100+profondeur)
    elif verifier_match_nul(plateau):
        return (None,0)
    if estMAX:
        
    
    
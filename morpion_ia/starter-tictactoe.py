# -*- coding: utf-8 -*-

import time
import Tictactoe 
from random import randint,choice

def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0

def RandomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles'''
    return choice(b.legal_moves())

def deroulementRandom(b):
    '''Effectue un déroulement aléatoire du jeu de morpion.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == "X":
            print("Victoire de X")
        elif res == "O":
            print("Victoire de O")
        else:
            print("Egalité")
        return
    b.push(RandomMove(b))
    deroulementRandom(b)
    b.pop()

def explore_game(board, results, moves=None):#parcourir toutes les parties possibles au Morpion(moves=None tous les coups possibles au début).
    if moves is None: 
        moves = []#liste vide si None.

    if board.is_game_over(): #on vérifie si le jeu est terminé
        result = board.result() #"1-0" || "0-1" || "1/2-1/2" les résultats.
        if result is None: #pas encore déterminé
            result = "tie" #égalitée donc
        results.append((moves, result)) #depuis cette instance,
        #on introduit le couple(moves,result) dans results qui est une liste.
        #result decrit le resultat de l'instance en cours,
        #moves decrit l'ensemble des coups possibles à partir de l'état actuel.
        return

    for move in board.legal_moves(): #pour chaque coup possible
        board.push(move) #on joue celui-là en le pushant
        explore_game(board, results, moves + [move])
        #appel récursif avec board results et moves qui devient moves+[move].
        board.pop()#on retire le coup.

board = Tictactoe.Board() #grille création.
results = [] #il contient les couples (coup,resultat) dont le nombre decrit l'ensemble des parties possibles.
explore_game(board, results) #explorer board avec results.

print(f"Nombre de parties: {len(results)}")
#255168 tournois possibles.

#board = Tictactoe.Board()
#print(board)

### Deroulement d'une partie aléatoire
#deroulementRandom(board)

#print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
#print(board)
#5 mis en comments.


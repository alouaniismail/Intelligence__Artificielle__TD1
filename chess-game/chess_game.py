import time
import chess
from random import randint, choice

def randomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles. Pour avoir un choix au hasard, il faut
    construire explicitement tous les mouvements. Or, generate_legal_moves() nous donne un itérateur.'''
    return choice([m for m in b.generate_legal_moves()])

def deroulementRandom(b):
    '''Déroulement d'une partie d'échecs au hasard des coups possibles. Cela va donner presque exclusivement
    des parties très longues et sans gagnant. Cela illustre cependant comment on peut jouer avec la librairie
    très simplement.'''
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    deroulementRandom(b)
    b.pop()

#board = chess.Board()
#deroulementRandom(board)

def randomEvaluation(b):
    return randint(-100, 100)

def searchLimited(b, depth, time_limit):
    nodes = 0
    if b.is_game_over() or depth == 0:
        return 1, randomEvaluation(b)
    start_time = time.time()
    for m in b.legal_moves:
        b.push(m)
        nodes_child, score_child = searchLimited(b, depth - 1, time_limit)
        nodes += nodes_child
        b.pop()
        if time.time() - start_time >= time_limit:
            break
    return nodes + 1, 0

board = chess.Board()
for depth in range(1, 10):
    nodes, _ = searchLimited(board, depth, 30)
    print(f"Profondeur {depth} : {nodes} noeuds")


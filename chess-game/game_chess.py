import chess
import chess.engine
import random

# Crée un moteur d'échecs Stockfish
engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")

# Définit la profondeur de recherche de l'IA
DEPTH = 3

# Fonction qui renvoie un coup aléatoire valide pour le joueur en cours
def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

# Fonction qui renvoie le meilleur coup pour l'IA en utilisant l'algorithme Minimax
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval, best_move

# Fonction qui évalue l'état actuel du plateau de jeu
def evaluate(board):
    # Votre fonction d'évaluation ici
    return random.uniform(-1, 1)

# Fonction qui joue un match entre un joueur humain et l'IA
def play_game():
    board = chess.Board()
    print(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = input("Votre coup : ")
            try:
                move = chess.Move.from_uci(move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Coup invalide")
            except:
                print("Coup invalide")
        else:
            _, move = minimax(board, DEPTH, float('-inf'), float('inf'), True)
            board.push(move)
        print(board)

    result = board.result()
    if result == "1-0":
        print("Blanc gagne")
    elif result == "0-1":
        print("Noir gagne")
    else:
        print("Partie nulle")

# Jouer un match
play_game()

# Ferme le moteur d'échecs
engine.quit()

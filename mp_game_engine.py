import random
from components import *

players = {}

def generate_attack():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print((x, y))
    return ((x, y))

def ai_opponent_game_loop():
    print("Welcome to the game Battleships!")

    board = initialize_board()
    ships = create_battleships()
    board = place_battleships(board, ships)
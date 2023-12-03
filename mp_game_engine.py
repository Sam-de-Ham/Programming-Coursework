import random
from components import *

players = {}

def generate_attack():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print((x, y))
    return ((x, y))

def ai_opponent_game_loop():
    print("Welcome to the game Battleships!\n")

    players["Player"] = (place_battleships(initialize_board(), create_battleships(), "custom"), create_battleships())
    players["AI"] = (place_battleships(initialize_board(), create_battleships(), "random"), create_battleships())

    print_2d_array(players["Player"][0])
    print_2d_array(players["AI"][0])

if __name__ == "__main__":
    ai_opponent_game_loop()
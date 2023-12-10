import random
from components import *
from game_engine import *

players = {}

def generate_attack():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return ((x, y))

def ai_opponent_game_loop():
    print("Welcome to the game Battleships!\n")

    players["Player"] = (place_battleships(initialise_board(), create_battleships(), "custom"), create_battleships())
    players["AI"] = (place_battleships(initialise_board(), create_battleships(), "random"), create_battleships())

    while game__not_over():
        coords = cli_coordinates_input()
        outcome = attack(coords, players["AI"][0], players["AI"][1])
        print("You hit a ship!\n\n" if outcome else "You missed!\n\n")

        coords = generate_attack()
        outcome = attack(coords, players["Player"][0], players["Player"][1])
        print_2d_array(players["Player"][0])
        print("AI hit a ship!\n\n" if outcome else "AI missed!\n\n")


def game__not_over():
    if all(value == 0 for value in players["Player"][1].values()):
        print("You lost!")
        return False
    elif all(value == 0 for value in players["AI"][1].values()):
        print("You won!")
        return False
    else:
        return True
    
def print_2d_array(arr_2d):
    col_widths = [max(len(str(row[i])) for row in arr_2d) for i in range(len(arr_2d[0]))]

    for row in arr_2d:
        print(" ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

if __name__ == "__main__":
    ai_opponent_game_loop()
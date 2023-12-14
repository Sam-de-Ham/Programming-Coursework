import random
from components import *
from game_engine import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

players = {}

def generate_attack(size = 10):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return ((x, y))

def ai_opponent_game_loop():
    # print('Welcome to the game Battleships!\n')
    logging.info('Welcome to the game Battleships!')

    players['player'] = {'board' : place_battleships(initialise_board(), create_battleships(), 'custom'), 'ships' : create_battleships()}
    players['AI'] = {'board' : place_battleships(initialise_board(), create_battleships(), 'random'), 'ships' : create_battleships()}

    while game__not_over():
        coords = cli_coordinates_input()
        outcome = attack(coords, players['AI']['board'], players['AI']['ships'])
        logging.info("You hit a ship!\n\n" if outcome else "You missed!\n")

        coords = generate_attack()
        outcome = attack(coords, players["player"]['board'], players["player"]['ships'])
        logging.info(f'{"AI hit a ship!" if outcome else "AI missed!"} Coordinates: {coords}\n')
        print('Current state of your board:')
        print_2d_array(players["player"]['board'])


def game__not_over():
    if all(value == 0 for value in players["player"]['ships'].values()):
        # print("You lost!")
        logging.info('You lost!')
        return False
    elif all(value == 0 for value in players["AI"]['ships'].values()):
        # print("You won!")
        logging.info('You won!')
        return False
    else:
        return True
    
def print_2d_array(arr_2d):
    col_widths = [max(len(str(row[i])) for row in arr_2d) for i in range(len(arr_2d[0]))]

    for row in arr_2d:
        print(" ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))
    print()

if __name__ == "__main__":
    ai_opponent_game_loop()
from components import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def attack(coordinates, board, battleships):
    x, y = coordinates
    if board[y][x] == None:
        logging.info('Attack missed')
        return False
    else:
        ship_name = board[y][x]
        battleships[ship_name] -= 1
        board[y][x] = None
        logging.info(f'Attach hit: {ship_name}')
        return True
    
def get_input(prompt, size = 10):
    while True:
        value = input(prompt)
        if value.isnumeric() and int(value) >= 0 and int(value) < size:
            return int(value)
        logging.warning('Input invalid, try again')

def cli_coordinates_input():
    x = get_input("Enter x coordinate: ")
    y = get_input("Enter y coordinate: ")
    return x, y

def simple_game_loop(size = 10):
    # print("Welcome to the game Battleships!")
    logging.info('Welcome to the game Battleships!')

    board = initialise_board(size)
    ships = create_battleships()
    place_battleships(board, ships)

    while not all(value == 0 for value in ships.values()):
        coords = cli_coordinates_input()
        outcome = attack(coords, board, ships)
        # print("Hit" if outcome else "Miss")
        # logging.info("Hit" if outcome else "Miss")
    # print("Game over")
    logging.info('Game over, you sunk all ships!')


if __name__ == "__main__":
    simple_game_loop(10)
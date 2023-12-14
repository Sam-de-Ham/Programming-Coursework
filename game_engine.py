from components import initialise_board, create_battleships, place_battleships

from typing import List, Dict, Tuple, Union
import config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def attack(coordinates: Tuple[int, int], board: List[List[Union[str, None]]], battleships: Dict[str, int]) -> bool:
    x, y = coordinates
    if board[y][x] == None:
        logging.info('Attack missed')
        return False
    else:
        ship_name = board[y][x]
        battleships[ship_name] -= 1
        board[y][x] = None
        logging.info(f'Attack hit: {ship_name}')
        return True
    
def get_input(prompt: str, size: int = 10) -> int:
    while True:
        value = input(prompt)
        if value.isnumeric() and 0 <= int(value) < size:
            return int(value)
        logging.warning('Input invalid, try again')

def cli_coordinates_input() -> Tuple[int, int]:
    x = get_input("Enter x coordinate: ")
    y = get_input("Enter y coordinate: ")
    return x, y

def simple_game_loop(size: int = 10) -> None:
    logging.info('Welcome to the game Battleships!')

    board = initialise_board(size)
    ships = create_battleships()
    place_battleships(board, ships)

    while not all(value == 0 for value in ships.values()):
        coords = cli_coordinates_input()
        outcome = attack(coords, board, ships)
    logging.info('Game over, you sunk all ships!')


if __name__ == "__main__":
    simple_game_loop(config.SIZE)
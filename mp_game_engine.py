from components import create_battleships, initialise_board, place_battleships
from game_engine import attack, cli_coordinates_input

from typing import List, Tuple, Union
import random
import config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

players = {}

def generate_attack(size: int = 10) -> Tuple[int, int]:
    """
    Generate a random attack position within a given size.

    Args:
        size (int): The size of the grid to generate the attack position on. Defaults to 10.

    Returns:
        Tuple[int, int]: A tuple representing the x and y coordinates of the generated attack position.
    """
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return ((x, y))

def ai_opponent_game_loop(size: int = 10) -> None:
    """
    Game loop for the AI opponent in the Battleships game.
    It sets up a dictionary with both users (player and AI), each having a board and ships dictionary.
    Until one of the players runs out of ships, the game continues to get input from the player,
    and random AI attacks. When one player wins, it is logged and the game ends.

    Parameters:
        size (int): The size of the game board. Defaults to 10.

    Returns:
        None

    """
    logging.info('Welcome to the game Battleships!')

    players['player'] = {'board' : place_battleships(initialise_board(size), create_battleships(), 'custom'), 'ships' : create_battleships()}
    players['AI'] = {'board' : place_battleships(initialise_board(size), create_battleships(), 'random'), 'ships' : create_battleships()}

    while game__not_over():
        coords = cli_coordinates_input()
        outcome = attack(coords, players['AI']['board'], players['AI']['ships'])
        logging.info("You hit a ship!\n\n" if outcome else "You missed!\n")

        coords = generate_attack(size)
        outcome = attack(coords, players["player"]['board'], players["player"]['ships'])
        logging.info(f'{"AI hit a ship!" if outcome else "AI missed!"} Coordinates: {coords}\n')
        print('Current state of your board:')
        print_2d_array(players["player"]['board'])

def game__not_over() -> bool:
    """
    Check that the game is not over. Used to loop the ai_opponent_game_loop.

    Returns:
        bool: True if the game is not over, False otherwise.
    """
    if all(value == 0 for value in players["player"]['ships'].values()):
        logging.info('You lost!')
        return False
    elif all(value == 0 for value in players["AI"]['ships'].values()):
        logging.info('You won!')
        return False
    else:
        return True
    
def print_2d_array(arr_2d: List[List[Union[str, None]]]) -> None:
    """
    Print a 2D array in a formatted way. This makes sure there is enough space for words.

    Parameters:
        arr_2d (List[List[Union[str, None]]]): A 2D array containing elements of type str or None.

    Returns:
        None: This function does not return anything.
    """
    col_widths = [max(len(str(row[i])) for row in arr_2d) for i in range(len(arr_2d[0]))]

    for row in arr_2d:
        print(" ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))
    print()

if __name__ == "__main__":
    ai_opponent_game_loop(config.SIZE)
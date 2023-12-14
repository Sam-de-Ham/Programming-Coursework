from components import initialise_board, create_battleships, place_battleships

from typing import List, Dict, Tuple, Union
import config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def attack(coordinates: Tuple[int, int], board: List[List[Union[str, None]]], battleships: Dict[str, int]) -> bool:
    """
    Performs a single attack on given the coordinates, board, and battleships.

    Parameters:
        coordinates (Tuple[int, int]): The x and y coordinates of the attack.
        board (List[List[Union[str, None]]]): The game board represented as a 2-d list.
        battleships (Dict[str, int]): A dictionary mapping the name of each battleship to its remaining health.

    Returns:
        bool: True if the attack hits a battleship, False otherwise.
    """
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
    """
    Function to get an integer input from the user within a specified range. Runs until valid input is provided.
    
    Args:
        prompt (str): The prompt to display to the user.
        size (int, optional): The upper limit of the range (exclusive). Defaults to 10.
        
    Returns:
        int: The integer input from the user.
    """
    while True:
        value = input(prompt)
        if value.isnumeric() and 0 <= int(value) < size:
            return int(value)
        logging.warning('Input invalid, try again')

def cli_coordinates_input() -> Tuple[int, int]:
    """
    A function that prompts the user to enter x and y coordinates.
    Uses the `get_input` function to get user input for the x and y coordinates.
    The function then returns a tuple containing the x and y coordinates.

    Returns:
        A tuple containing the x and y coordinates entered by the user.
    """
    x = get_input("Enter x coordinate: ")
    y = get_input("Enter y coordinate: ")
    return x, y

def simple_game_loop(size: int = 10) -> None:
    """
    This function represents a simple game loop for the game Battleships.
    It takes an optional parameter `size` which specifies the size of the game board (default is 10).

    The main loop of the game continues until all the ships have been sunk. Inside the loop,
    the function prompts the player for coordinates using the `cli_coordinates_input` function,
    and then attacks the specified coordinates by calling the `attack` function.

    Finally, when all the ships have been sunk, the function logs a game over message.

    Parameters:
        size (int): The size of the game board. Defaults to 10.

    Returns:
        None
    """
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
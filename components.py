"""
components.py - Module for core game components

This module provides functions for managing game components such as initializing a game board,
creating battleships, placing battleships on the board, and checking if the board is empty.

Functions:
- initialise_board: Initializes a square game board of a specified size.
- create_battleships: Reads a file containing battleship names and their lengths,
  and returns a dictionary mapping each battleship to its length.
- place_battleships: Generates the placement of battleships on the board
  according to the specified algorithm.
- place_custom_single_ship: Place a single custom ship on the board.
- place_random_single_ship: Randomly places a single ship on the board.
- check_empty: Check if the given board is empty.
"""

from typing import List, Dict, Tuple, Union
import random
import json
import logging
import config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def initialise_board(size: int = 10) -> List[List[Union[str, None]]]:
    """
    Initializes a square game board of a specified size.

    Args:
        size (int): The size of the game board. Defaults = 10.

    Returns:
        List[List[Union[str, None]]]: A 2D list representing the game board,
        with each element initialized to None.

    Raises:
        ValueError: If the size is less than 1 or not an integer.
    """
    if size < 1 or isinstance(size, int) is False:
        logging.error('Size must be a positive integer')
        raise ValueError('Size must be a positive integer')
    board = [[None for _ in range(size)] for _ in range(size)]
    return board

def create_battleships(filename: str = config.BATTLESHIPS) -> Dict[str, int]:
    """
    Reads a file containing battleship names and their lengths, and returns a dictionary
    mapping each battleship to its length.

    Args:
        filename (str, optional): The path to the file containing the battleships data.
            Defaults to 'battleships.txt' which is stored in the config.

    Returns:
        Dict[str, int]: A dictionary mapping each battleship name to its length.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If an error occurs while creating the battleships dictionary.
    """
    ships = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file_in:
            for line in file_in:
                ships[line.split(":")[0]] = int(line.split(":")[1])
        logging_message = f'Battleships loaded from: {filename}'
        logging.info(logging_message)
    except FileNotFoundError as filenotfound:
        error_message = f'File not found: {filename}'
        logging.error(error_message)
        raise filenotfound
    except Exception as exception:
        error_message = f'An error occured while creating battlefships: {exception}'
        logging.error(error_message)
        raise exception
    return ships

def place_battleships(board: List[List[Union[str, None]]], ships: Dict[str, int],
                      algorithm: str = config.ALGORITHM_SIMPLE) -> List[List[Union[str, None]]]:
    """
    Generates the placement of battleships on the board according to the specified algorithm.

    Args:
        board (List[List[Union[str, None]]]): The game board represented as a 2-d list.
        ships (Dict[str, int]): A dictionary containing the names of the ships as keys
        and the number of each ship as values.
        algorithm (str, optional): The algorithm to use for placing the ships.
        Defaults to 'simple' which is stored in the config.

    Returns:
        List[List[Union[str, None]]]: The updated game board with the battleships placed.
    """
    if algorithm == config.ALGORITHM_SIMPLE:
        for i, (key, value) in enumerate(ships.items()):
            for j in range(value):
                board[i][j] = key
        return board

    if algorithm == config.ALGORITHM_RANDOM:
        for boat_name, boat_size in ships.items():
            place_random_single_ship(board, boat_name, boat_size)
        return board

    if algorithm == config.ALGORITHM_CUSTOM:
        try:
            with open(config.PLACEMENT, 'r', encoding='utf-8') as file:
                placements = json.load(file)
        except FileNotFoundError as filenotfound:
            logging.error('placement.json file not found')
            error_message = f'placement.json file not found: {filenotfound}'
            raise FileNotFoundError(error_message) from filenotfound

        for boat_name, boat_size in ships.items():
            place_custom_single_ship(board, boat_name, boat_size, placements[boat_name])
        return board
    return None

def place_custom_single_ship(board: List[List[Union[str, None]]], boat_name: str,
                             boat_size: int, placement: Tuple[str, str, str]) -> None:
    """
    Place a single custom ship on the board. Used by place_battleships()
    when using the 'custom' algorithm.

    Args:
        board (List[List[Union[str, None]]]): The game board represented as a 2-d list.
        boat_name (str): The name of the ship to be placed.
        boat_size (int): The size of the ship to be placed.
        placement (Tuple[str, str, str]): A tuple representing the placement of the ship. 
        The first element is the x-coordinate, the second element is the y-coordinate, 
        and the third element is the orientation ('h' for horizontal, 'v' for vertical).

    Returns:
        None

    Raises:
        ValueError: If the placement is invalid.

    """
    x_placement = int(placement[0])
    y_placement = int(placement[1])

    if placement[2] == 'h':
        for i in range(boat_size):
            if board[y_placement][x_placement + i] is not None:
                logging.error('Invalid placement')
                raise ValueError('Invalid placement')

        for i in range(boat_size):
            board[y_placement][x_placement + i] = boat_name

    if placement[2] == 'v':
        for i in range(boat_size):
            if board[y_placement + i][x_placement] is not None:
                logging.error('Invalid placement')
                raise ValueError('Invalid placement')

        for i in range(boat_size):
            board[y_placement + i][x_placement] = boat_name


def place_random_single_ship(board: List[List[Union[str, None]]],
                            boat_name: str, boat_size: int) -> None:
    """
    Randomly places a single ship on the board. Used by place_battleships()
    when using the 'random' algorithm.
    
    Args:
        board (List[List[Union[str, None]]]): The game board represented as a 2-d list.
        boat_name (str): The name of the ship to be placed.
        boat_size (int): The size of the ship to be placed.
    
    Returns:
        None
    """
    direction = random.choice(['horizontal', 'vertical'])
    if direction == 'horizontal':
        board_size = len(board)
        available_rows = board_size
        available_cols = board_size - boat_size + 1

        row = random.randint(0, available_rows - 1)
        col = random.randint(0, available_cols - 1)

        for i in range(boat_size):
            if board[row][col + i] is not None:
                logging.debug('Invalid placement. Retrying...')
                return place_random_single_ship(board, boat_name, boat_size)
        for i in range(boat_size):
            board[row][col + i] = boat_name

    elif direction == 'vertical':
        board_size = len(board)
        available_rows = board_size - boat_size + 1
        available_cols = board_size

        row = random.randint(0, available_rows - 1)
        col = random.randint(0, available_cols - 1)

        for i in range(boat_size):
            if board[row + i][col] is not None:
                logging.debug('Invalid placement. Retrying...')
                return place_random_single_ship(board, boat_name, boat_size)
        for i in range(boat_size):
            board[row + i][col] = boat_name
    return None

def check_empty(board: List[List[Union[str, None]]]) -> bool:
    """
    Check if the given board is empty.

    Args:
        board (List[List[Union[str, None]]]): The game board represented
        as a 2-d list which is to be checked.

    Returns:
        bool: True if the board is empty, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell is not None:
                return False
    return True

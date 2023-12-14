import random
import json
import logging
import config
from typing import List, Dict, Tuple, Union

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def initialise_board(size: int = 10) -> List[List[Union[str, None]]]:
    if size < 1 or isinstance(size, int) is False:
        logging.error('Size must be a positive integer')
        raise ValueError('Size must be a positive integer')
    board = [[None for _ in range(size)] for _ in range(size)]
    return board

def create_battleships(filename: str = config.BATTLESHIPS) -> Dict[str, int]:
    ships = {}
    try:
        with open(filename) as file_in:
            for line in file_in:
                ships[line.split(":")[0]] = int(line.split(":")[1])
        logging.info(f'Battleships loaded from: {filename}')
    except FileNotFoundError as filenotfound:
        logging.error(f'File not found: {filename}')
        raise filenotfound
    except Exception as e:
        logging.error(f'An error occured while creating battlefships: {e}')
        raise e
    return ships

def place_battleships(board: List[List[Union[str, None]]], ships: Dict[str, int],
                      algorithm: str = config.ALGORITHM_SIMPLE) -> List[List[Union[str, None]]]:
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
            with open(config.PLACEMENT, 'r') as file:
                placements = json.load(file)  
        except FileNotFoundError as filenotfound:
            logging.error('placement.json file not found')
            raise FileNotFoundError(f'placement.json file not found: {filenotfound}')

        for boat_name, boat_size in ships.items():
            place_custom_single_ship(board, boat_name, boat_size, placements[boat_name])
        return board

def place_custom_single_ship(board: List[List[Union[str, None]]], boat_name: str,
                             boat_size: int, placement: Tuple[str, str, str]) -> None:
    x = int(placement[0])
    y = int(placement[1])
    
    if placement[2] == 'h':
        for i in range(boat_size):
            if board[y][x + i] is not None:
                logging.error('Invalid placement')
                raise ValueError('Invalid placement')
        
        for i in range(boat_size):
            board[y][x + i] = boat_name

    if placement[2] == 'v':
        for i in range(boat_size):
            if board[y + i][x] is not None:
                logging.error('Invalid placement')
                raise ValueError('Invalid placement')
        
        for i in range(boat_size):
            board[y + i][x] = boat_name


def place_random_single_ship(board: List[List[Union[str, None]]], boat_name: str, boat_size: int) -> None:
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

def check_empty(board: List[List[Union[str, None]]]) -> bool:
    for row in board:
        for cell in row:
            if cell is not None:
                return False
    return True
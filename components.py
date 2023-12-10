import random
import json

def initialise_board(size = 10):
    if size < 1:
        raise ValueError("Size must be a positive integer")
    board = [[None for _ in range(size)] for _ in range(size)]
    return board

def create_battleships(filename = "battleships.txt"):
    ships = {}
    with open(filename) as file_in:
        for line in file_in:
            ships[line.split(":")[0]] = int(line.split(":")[1])
    return ships

def place_battleships(board, ships, algorithm = "simple"):
    if algorithm == "simple":
        for i, (key, value) in enumerate(ships.items()):
            for j in range(value):
                board[i][j] = key
        return board

    if algorithm == "random":
        for boat_name, boat_size in ships.items():
            place_random_single_ship(board, boat_name, boat_size)
        return board
    
    if algorithm == "custom": 
        with open('placement.json', 'r') as file:
            placements = json.load(file)  
    
        for boat_name, boat_size in ships.items():
            place_custom_single_ship(board, boat_name, boat_size, placements[boat_name])
        return board
    

def place_custom_single_ship(board, boat_name, boat_size, placement):
    if placement is None:
        raise ValueError("Invalid placement")
    
    placement[0] = int(placement[0])
    placement[1] = int(placement[1])
    
    if placement[2] == "h":
        for i in range(boat_size):
            if board[placement[1]][placement[0] + i] is not None:
                raise ValueError("Invalid placement")
        
        for i in range(boat_size):
            board[placement[1]][placement[0] + i] = boat_name

    if placement[2] == "v":
        for i in range(boat_size):
            if board[placement[1] + i][placement[0]] is not None:
                raise ValueError("Invalid placement")
        
        for i in range(boat_size):
            board[placement[1] + i][placement[0]] = boat_name


def place_random_single_ship(board, boat_name, boat_size):
    direction = random.choice(['horizontal', 'vertical'])
    if direction == "horizontal":
        board_size = len(board)
        available_rows = board_size
        available_cols = board_size - boat_size + 1
    
        row = random.randint(0, available_rows - 1)
        col = random.randint(0, available_cols - 1)

        for i in range(boat_size):
            if board[row][col + i] is not None:
                return place_random_single_ship(board, boat_name, boat_size)
        for i in range(boat_size):
            board[row][col + i] = boat_name
    
    elif direction == "vertical":
        board_size = len(board)
        available_rows = board_size - boat_size + 1
        available_cols = board_size

        row = random.randint(0, available_rows - 1)
        col = random.randint(0, available_cols - 1)

        for i in range(boat_size):
            if board[row + i][col] is not None:
                return place_random_single_ship(board, boat_name, boat_size)
        for i in range(boat_size):
            board[row + i][col] = boat_name

def check_empty(board):
    for row in board:
        for cell in row:
            if cell is not None:
                return False
    return True
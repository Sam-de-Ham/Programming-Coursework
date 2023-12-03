def initialize_board(size = 10):
    board = [[None for _ in range(size)] for _ in range(size)]
    return board

def create_battleships(filename = "battleships.txt"):
    ships = {}
    with open(filename) as file_in:
        for line in file_in:
            ships[line.split(":")[0]] = int(line.split(":")[1])
    return ships

def place_battleships(board, ships, algorithm = "simple"):
    for i, (key, value) in enumerate(ships.items()):
        for j in range(value):
            board[i][j] = key
    return board
from components import *

def attack(coordinates, board, battleships):
    x, y = coordinates
    if board[y][x] == None:
        return False
    else:
        battleships[board[y][x]] = battleships[board[y][x]] - 1
        board[y][x] = None
        return True
    
def get_input(prompt):
    while True:
        value = input(prompt)
        if value.isnumeric() and int(value) >= 0 and int(value) < 10:
            return int(value)

def cli_coordinates_input():
    x = get_input("Enter x coordinate: ")
    y = get_input("Enter y coordinate: ")
    return x, y

def simple_game_loop(size):
    print("Welcome to the game Battleships!")

    board = initialize_board()
    ships = create_battleships()
    place_battleships(board, ships)

    while not all(value == 0 for value in ships.values()):
        coords = cli_coordinates_input()
        outcome = attack(coords, board, ships)
        print("Hit" if outcome else "Miss")
    print("Game over")


if __name__ == "__main__":
    simple_game_loop(10)
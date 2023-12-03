from components import *

def attack(coordinates, board, battleships):
    x, y = coordinates
    if board[y][x] == None:
        return False
    else:
        battleships[board[y][x]] = battleships[board[y][x]] - 1
        board[y][x] = None
        return True
    
def cli_coordinates_input():
    x = int(input("x: "))
    y = int(input("y: "))
    return x, y

def simple_game_loop():
    print("Welcome to the game Battleships!")

    board = initialize_board()
    ships = create_battleships()
    board = place_battleships(board, ships)

    while not all(value == 0 for value in ships.values()):
        coords = cli_coordinates_input()
        outcome = attack(coords, board, ships)
        print("Hit" if outcome else "Miss")
        for row in board:
            print(row)

    print("Game over")

if __name__ == "__main__":
    simple_game_loop()
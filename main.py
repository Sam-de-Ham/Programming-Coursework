"""
main.py - Module for the main application logic of the Battleships game

This module defines the Flask application and handles the routes
and endpoints for the Battleships game.
It includes functions for handling ship placement, attacking, and rendering the game interface.

Functions:
- placement_interface: Endpoint for the '/placement' route that handles ship placement.
- root: Function that handles the root '/' endpoint of the application.
- process_attack: Function that processes an attack '/attack' on the game board.
"""

import json
import logging
from typing import List, Dict, Union, Any
from flask import Flask, render_template, request, jsonify, redirect

import config
from components import initialise_board, create_battleships, place_battleships, check_empty
from game_engine import attack
from mp_game_engine import generate_attack

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

board_initialized: bool = False
player_board: List[List[Union[str, None]]] = []
ai_board: List[List[Union[str, None]]] = []
ships: Dict[str, int] = {}

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface() -> Any:
    """
    Endpoint for the '/placement' route that handles both GET and POST requests.
    For 'GET' requests it renders the 'placement.html' template.
    For 'POST' requests it reads the JSON data from the response
    and writes it to the ships placement file.
    
    Parameters:
    json data (Dict[str, Any]): The JSON data sent in the POST request
    
    Returns:
    Flask.Response: 'GET' : The 'placement.html' template rendered
                            with the correct size and ships to place.
                    'POST' : message indicating the JSON data was received.
    """
    # global player_board, ai_board, ships, board_initialized

    if request.method == 'GET':
        ships = create_battleships()
        logging_message = f'Rendering {config.PLACEMENT_HTML} for ship placement'
        logging.info(logging_message)
        return render_template(config.PLACEMENT_HTML, ships=ships, board_size=10)

    if request.method == 'POST':
        data: Dict[str, Any] = request.get_json()

        with open(config.PLACEMENT, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file)

        if not board_initialized:
            player_board = initialise_board(size = 10)
            ai_board = initialise_board(size = 10)

            player_board = place_battleships(player_board, ships, "custom")
            ai_board = place_battleships(ai_board, ships, "random")
            board_initialized = True
            logging.info('Boards initialized and battleships placed')

        return jsonify({'message': 'Received'}), 200
    return None

@app.route('/', methods=['GET'])
def root() -> Any:
    """
    A function that handles the root endpoint of the application.
    If the board has not been created the user is redirected to /placement to do so
    If it has, then it will render the main page. 

    Parameters:
    None

    Returns:
    Flask.Response: redirects to /placement if the board has not been created
                    render the main page if the board has been created previously
    """
    global board_initialized

    if request.method == 'GET':
        if board_initialized:
            logging_message = f'Rendering {config.MAIN_HTML} for gameplay'
            logging.info(logging_message)
            return render_template(config.MAIN_HTML, player_board=player_board)
        else:
            logging_message = f'Redirecting to {config.PLACEMENT_HTML} for ship placement'
            logging.info(logging_message)
            return redirect('/placement')
    return None

@app.route('/attack', methods=['GET'])
def process_attack() -> Any:
    """
    Process an attack on the game board.
    Takes the clicked coordinates from user and attacks that place on AI board.
    Creates an AI attack and attacks player board accordingly.
    Returns the response in JSON format with accompanying logging. 

    Parameters:
    x (int): The x coordinate of the attack.
    y (int): The y coordinate of the attack.

    Returns:
    JSON: information about the outcome of the attack, and the state of the game
    """
    global player_board, ai_board

    if request.method == 'GET':
        x_coordinate = int(request.args.get('x'))
        y_coordinate = int(request.args.get('y'))

        outcome = attack((x_coordinate, y_coordinate), ai_board, ships)
        logging_message = (f'Player attacked AI at coordinates: {x_coordinate}, {y_coordinate}. '
                            f'Outcome: {"Hit" if outcome else "Miss"}')
        logging.info(logging_message)

        if check_empty(ai_board):
            logging.info('Game Over, player won')
            return jsonify({'hit': True, 'Player_Turn': (x_coordinate, y_coordinate),
                            'finished': 'Game Over Player wins'})

        ai_coordinates = generate_attack(config.SIZE)
        attack(ai_coordinates, player_board, ships)
        logging_message = f'AI attacked player at coordinates: {ai_coordinates}'
        logging.info(logging_message)

        if check_empty(player_board):
            logging.info('Game Over, AI won')
            return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates,
                            'finished': 'Game Over AI wins'})

        return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates})
    return None

if __name__ == '__main__':
    app.run(debug=True)

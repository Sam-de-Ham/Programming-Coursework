from components import initialise_board, create_battleships, place_battleships, check_empty
from game_engine import attack
from mp_game_engine import generate_attack

from typing import List, Dict, Union, Any
from flask import Flask, render_template, request, jsonify, redirect
import json
import config
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

board_initialized: bool = False
player_board: List[List[Union[str, None]]]

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface() -> Flask.Response:
    global player_board, ai_board, ships, board_initialized

    if request.method == 'GET':
        ships = create_battleships()
        logging.info(f'Rendering {config.PLACEMENT_HTML} for ship placement')
        return render_template(config.PLACEMENT_HTML, ships=ships, board_size=10)

    elif request.method == 'POST':
        data: Dict[str, Any] = request.get_json()

        with open(config.PLACEMENT, 'w') as json_file:
            json.dump(data, json_file)

        if not board_initialized:
            player_board = initialise_board(size = 10)
            ai_board = initialise_board(size = 10)

            player_board = place_battleships(player_board, ships, "custom")
            ai_board = place_battleships(ai_board, ships, "random")
            board_initialized = True
            logging.info('Boards initialized and battleships placed')
        
        return jsonify({'message': 'Received'}), 200
    


@app.route('/', methods=['GET'])
def root() -> Flask.Response:
    global board_initialized

    if request.method == 'GET':
        global board_initialized

        if board_initialized:
            logging.info(f'Rendering {config.MAIN_HTML} for gameplay')
            return render_template(config.MAIN_HTML, player_board=player_board)
        else:
            logging.info(f'Redirecting to {config.PLACEMENT_HTML} for ship placement')
            return redirect('/placement')

@app.route('/attack', methods=['GET'])
def process_attack() -> Any:
    global player_board, ai_board

    if request.method == 'GET':
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))

        outcome = attack((x, y), ai_board, ships)
        logging.info(f'Player attacked AI at coordinates: {x}, {y}. Outcome: {"Hit" if outcome else "Miss"}')

        if check_empty(ai_board):
            logging.info('Game Over, player won')
            return jsonify({'hit': True, 'Player_Turn': (x, y), 'finished': 'Game Over Player wins'})

        ai_coordinates = generate_attack(config.SIZE)
        attack(ai_coordinates, player_board, ships)
        logging.info(f'AI attacked player at coordinates: {ai_coordinates}')

        if check_empty(player_board):
            logging.info('Game Over, AI won')
            return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates, 'finished': 'Game Over AI wins'})
        
        return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates})

if __name__ == '__main__':
    app.run(debug=True)
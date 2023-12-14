from flask import Flask, render_template, request, jsonify, redirect
from components import initialise_board, create_battleships, place_battleships, check_empty
from game_engine import attack
from mp_game_engine import generate_attack
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

board_initialized = False

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    global player_board, ai_board, ships, board_initialized

    if request.method == 'GET':
        ships = create_battleships()
        logging.info('Rendering placement.html for ship placement')
        return render_template('placement.html', ships=ships, board_size=10)

    elif request.method == 'POST':
        data = request.get_json()

        with open("placement.json", 'w') as json_file:
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
def root():
    global board_initialized

    if request.method == 'GET':
        global board_initialized

        if board_initialized:
            logging.info('Rendering main.html for gameplay')
            return render_template('main.html', player_board=player_board)
        else:
            logging.info('Redirecting to placement.html for ship placement')
            return redirect('/placement')

@app.route('/attack', methods=['GET'])
def process_attack():
    global player_board, ai_board

    if request.method == 'GET':
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))

        outcome = attack((x, y), ai_board, ships)
        logging.info(f'Player attacked AI at coordinates: {x}, {y}. Outcome: {"Hit" if outcome else "Miss"}')

        if check_empty(ai_board):
            # print("Game Over, player won")
            logging.info('Game Over, player won')
            return jsonify({'hit': True, 'Player_Turn': (x, y), 'finished': 'Game Over Player wins'})

        ai_coordinates = generate_attack()
        attack(ai_coordinates, player_board, ships)
        logging.info(f'AI attacked player at coordinates: {ai_coordinates}')

        if check_empty(player_board):
            # print("Game Over, AI won")
            logging.info('Game Over, AI won')
            return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates, 'finished': 'Game Over AI wins'})
        
        return jsonify({'hit': outcome, 'AI_Turn': ai_coordinates})

if __name__ == '__main__':
    app.run(debug=True)
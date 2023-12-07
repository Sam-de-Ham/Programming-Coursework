from flask import Flask, render_template, request, jsonify
from components import initialize_board, create_battleships, place_battleships
from game_engine import attack

app = Flask(__name__)

@app.route('/')
def root():
    player_board = initialize_board()
    return render_template('main.html', player_board=player_board)

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'GET':
        return render_template('placement.html')
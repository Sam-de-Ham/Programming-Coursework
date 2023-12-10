from flask import Flask, render_template, request, jsonify, redirect
from components import *
from game_engine import *
from mp_game_engine import generate_attack
import json

app = Flask(__name__)

board_initialised = False

@app.route("/placement", methods = ["GET", "POST"])
def placement_interface():
    global board_initialised, player_board, ships

    if request.method == "GET":

        ships = create_battleships()
        board_size = 10
        return render_template("placement.html", ships = ships, board_size = 10)
    
    elif request.method == "POST":
        data = request.get_json()

        with open("placement.json", "w") as json_file:
            json.dump(data, json_file)

        if not board_initialised:
            player_board = initialise_board(size = 10)
            player_board = place_battleships(player_board, ships, "custom")
            board_initialised = True

        return jsonify(("Placement", "received", 200))
    
@app.route("/", methods = ["GET"])
def root():

    global board_initialised

    if request.method == "GET":
        if board_initialised:
            return render_template("main.html", player_board = player_board)
        else:
            return redirect("/placement")

    
if __name__ == "__main__":
    app.run(debug = True)
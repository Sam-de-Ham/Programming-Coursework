from flask import Flask, render_template, request, jsonify, redirect
from components import initialize_board, create_battleships, place_battleships
from game_engine import attack

app = Flask(__name__)

# Replace these global variables with appropriate usage
# based on your game logic and player boards
player_board = initialize_board()
ships = create_battleships()
board_initialized = False

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    global player_board, ships, board_initialized

    if request.method == 'GET':
        # Render the placement.html template with required parameters
        return render_template('placement.html', ships=ships, board_size=10)

    elif request.method == 'POST':
        data = request.get_json()

        # Use the incoming data and interact with game logic
        # Update player_board or other variables based on your game logic

        # For example, update the board with received data
        if not board_initialized:
            player_board = initialize_board()  # Initialize board if not done
            player_board = place_battleships(player_board, ships, "custom")  # Place ships based on received data
            board_initialized = True
        
        # Return a success message to the template
        return jsonify({'message': 'Received'}), 200

@app.route('/', methods=['GET'])
def root():
    global board_initialized

    if request.method == 'GET':
        global board_initialized

        # If the board is initialized, render the main.html template
        if board_initialized:
            return render_template('main.html', player_board=player_board)
        else:
            # If the board is not initialized, redirect to the placement interface
            return redirect('/placement')

@app.route('/attack', methods=['GET'])
def process_attack():
    global player_board

    if request.method == 'GET':
        # Retrieve the X and Y coordinates from the request arguments
        x = request.args.get('x')
        y = request.args.get('y')

        # Use these coordinates to interact with your game logic
        # Perform attack logic here and update player_board

        # Example: Attack logic
        outcome = attack((x, y), player_board, ships)
        # Further logic based on the outcome of the attack

        # Prepare response based on game status
        # Return JSON response based on game status
        # Example: Return JSON response for attack status
        return jsonify({'hit': outcome, 'AI_Turn': (1, 2)})
        # Update 'finished' if game over condition is met

if __name__ == '__main__':
    app.run(debug=True)

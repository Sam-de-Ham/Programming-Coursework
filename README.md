# Programming-Coursework - Battleship Game with Flask UI

## Metadata
GitHub Repository - https://github.com/Sam-de-Ham/Programming-Coursework 

Course : ECM1400 - Programming

Student Name : Samuel Weisz

Student Number : 730040759

Date of Submission : 15/12/2023

## Features Completed
- GitHub repository
- Readme
- Requirements.txt
- Expanded on unit testing
- Type hinting
- Object Oriented Programming for flow
- Doc string comments
- Config file
- Simple game loop (one board one player)
- CLI AI game loop
- Flask game - player vs AI with UI
- Flask integration
- Input validation
- Error handling
- Logging
- All required functions, plus helper functions
    - components.py
        - initialize_board()
        - create_battleships()
        - place_battleships()
        - place_custom_single_ship()
        - place_random_single_ship()
        - check_empty()
    - game_engine.py
        - attack()
        - get_input()
        - cli_coordinates_input()
        - simple_game_loop()
    - mp_game_engine.py
        - generate_attack()
        - ai_opponent_game_loop()
        - game_not_over()
        - print_2d_array()
    - main.py
        - Class: BattleshipsGame
            - __init__()
            - placement_interface()
            - root()
            - process_attack()
        - placement_interface()
        - root()
        - process_attack()


## Self-Assesment

## Overview
The Battleship game is a multiplayer game where players take turns trying to sink each other's battleships on a tiled square game board. This project creates the logic for this game in Python, and then connects it to a UI through Flask. 

## Structure
### config.py
This module contains configuration variables used in the game, such as the size of the board, file paths, and algorithm names.

### components.py
This module contains the most basic components of the game logic, including functions to create the board, and place ships.

### game_engine.py
THis module manages the core game logic, combining functions from components.py into the foundation of the game. 

### mp_game_engine.py 
This module uses game_engine.py to create multiplayer logic for the game, including attacking adn running simple game loops. 

### main.py 
This module is responsible for the main application logic. It defines the Flask application and handles routes/endpoints for the game, integrating the other files. 

## Requirements
- Python 3+
- Libraries can be installed from requirements.txt 
    - Run 'pip install -r requirements.txt' in cmd
    - Required libraries:
        - Flask==2.2.2
        - pytest==7.4.0

## Getting Started
To run the prject, follow these steps:
1. Make sure you have Python 3 installed
2. Clone/unzip this repository to your local machine
3. Install the required dependencies by running 'pip install -r requirements.txt' (Flask==2.2.2, pytest==7.4.0)
4. Run the game by executing 'python main.py' in the main project directory
5. Access the game through a web browser at http://127.0.0.1:5000/

## License
All rights reserved. 
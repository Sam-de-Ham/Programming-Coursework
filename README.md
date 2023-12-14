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
Looking back at the project I am extremely happy with how it came together. Through multiple iterations, I believe I have made a well-organized project, including a good README, and GitHub repository. Overall I have expanded on features in multiple ways, including adding additional pytest tests, using object oriented programming in main.py for better flow and variable scope, and adding a requirements.txt for ease of use. If I had more time, though, I do think I could improve the project in some key ways, for instance making the Flask UI more pleasing to look at, and adding better AI attacking/placement algorithms. Overall, I do however that my product is high quality, and meets all requirements at a high level. My code is written in an understandeable, robust, and modular way. 

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
4. Follow either 'How to use Flask version' or 'How to use CMD version (ai_opponent_game_loop)' for either version of the game. 

## How to use Flask version
1. Run the game by executing 'python main.py' in the main project directory
2. Access the game through a web browser at http://127.0.0.1:5000/
3. Place all ships by left clicking fields and pressing r to rotate
4. Click 'send game' to confirm placement
5. Attack the AI on the left field until either the player or AI wins (error message will be displayed)

## How to use CMD version (ai_opponent_game_loop)
1. Run mp_game_engine.py
2. Enter guess for x, then y coordinates to attack in CMD
3. Look at enemie's attack and the status of your board
4. Continue until win message for either player is displayed.

## License
All rights reserved. 
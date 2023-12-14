"""
config.py - Configuration file for the Battleships game

This module defines the configuration variables used in the Battleships game.
"""

# Numbers
SIZE = 10 # size of board

# Files
BATTLESHIPS = 'battleships.txt' # file with battleships
PLACEMENT = 'placement.json' # file with placement of ships

# Algorithms
ALGORITHM_SIMPLE = 'simple' # algorithm that places sequetially
ALGORITHM_RANDOM = 'random' # algorithm that places randomly
ALGORITHM_CUSTOM = 'custom' # algorithm that places according to placement.json

# HTML files
PLACEMENT_HTML = 'placement.html' # html file for placing ships
MAIN_HTML = 'main.html' # html file for gameplay

"""
This module contains extension tests for the functionality of the project's code.
"""

import importlib
import pytest
import tests.test_helper_functions as thf

testReport = thf.TestReport("test_report_extension.txt")

# Added tests for components.py

@pytest.mark.dependency()
def test_components_exists():
    """
    Test if the components module exists.
    """
    try:
        importlib.import_module('components')
    except ImportError:
        pytest.fail("components module does not exist")

from components import initialise_board

@pytest.mark.dependency(depends=["test_components_exists"])
def test_initialise_board_negative_size():
    """
    Test if ValueError is raised when the size is negative.
    """
    with pytest.raises(ValueError):
        initialise_board(-5)


@pytest.mark.dependency(depends=["test_components_exists"])
def test_initialise_board_string_size():
    """
    Test if ValueError is raised when the size is a string.
    """
    with pytest.raises(ValueError):
        initialise_board('test')

from components import check_empty

def test_check_empty_empty_board():
    """
    Test if the function correctly identifies an empty board.
    """
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    assert check_empty(board) is True

def test_check_empty_non_empty_board():
    """
    Test if the function correctly identifies a non-empty board.
    """
    board = [[None, None, None],
             [None, 'X', None],
             [None, None, None]]
    assert check_empty(board) is False


# Added tests for mp_game_engine.py
from mp_game_engine import generate_attack
def test_generate_attack_within_range():
    """
    Test if the generated attack position is within the specified size.
    """
    size = 10
    attack = generate_attack(size)
    x_coord, y_coord = attack
    assert 0 <= x_coord < size
    assert 0 <= y_coord < size

def test_generate_attack_default_size():
    """
    Test if the generated attack position is within the default size of 10.
    """
    attack = generate_attack()
    x_coord, y_coord = attack
    assert 0 <= x_coord < 10
    assert 0 <= y_coord < 10

def test_generate_attack_randomness():
    """
    Test if the generated attack positions are different across multiple calls.
    """
    size = 10
    attack1 = generate_attack(size)
    attack2 = generate_attack(size)
    assert attack1 != attack2

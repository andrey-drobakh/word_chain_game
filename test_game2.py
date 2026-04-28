
from game2 import _get_next_index, _is_word_correct


def test_get_next_index() :
    current_index = 1
    player_names = ['John', 'Tom', 'Alex', 'Pit']
    assert _get_next_index( current_index, player_names ) == 2


def test_get_next_i() :
    current_index = 3
    player_names = ['John', 'Tom', 'Alex', 'Pit']
    assert _get_next_index( current_index, player_names ) == 0


def test_is_word_correct() :
    pass




from game import _get_next_index, _is_word_correct


def test_get_next_index() :
    player_names = ['John', 'Tom', 'Alex', 'Pit']

    assert _get_next_index( 0, player_names ) == 1
    assert _get_next_index( 1, player_names ) == 2
    assert _get_next_index( 2, player_names ) == 3
    assert _get_next_index( 3, player_names ) == 0





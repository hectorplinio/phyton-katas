from src.findMaxNumber.findMaxNumber import find_max_number


def test_default_max_number():
    assert find_max_number() == 5


def test_given_input_params():
    assert find_max_number([10, 20, 30, 40, 50]) == 50


def test_with_negative_numbers():
    assert find_max_number([-1, -2, -3, -4, -5]) == -1


def test_with_mixed_numbers():
    assert find_max_number([-10, 0, 10, 20, 30]) == 30


def test_empty_list():
    assert find_max_number([]) == 0

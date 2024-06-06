from src.sumNumbers.sumNumbers import sum_numbers


def test_sum_numbers_default():
    assert sum_numbers() == 15


def test_sum_numbers_given_input():
    assert sum_numbers([10, 20, 30]) == 60


def test_sum_numbers_empty_input():
    assert sum_numbers([]) == 0


def test_sum_numbers_single_element():
    assert sum_numbers([42]) == 42

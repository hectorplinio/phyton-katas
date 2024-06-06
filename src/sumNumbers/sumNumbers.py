from typing import List


initial_object = [1, 2, 3, 4, 5]


def sum_numbers(input_params: List[int] = initial_object) -> int:
    sum = 0
    for number in input_params:
        sum = sum + number
    return sum

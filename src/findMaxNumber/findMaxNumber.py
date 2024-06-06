from typing import List

initial_object = [1, 2, 3, 4, 5]


def find_max_number(input_params: List[int] = initial_object) -> int:
    max_number = input_params[0] if input_params else 0
    for number in input_params:
        if number > max_number:
            max_number = number
    return max_number

from typing import List
import numpy as np

preamble_length = 25


def find_combinations(numbers: List[str]) -> List[int]:
    numbers = np.array(list(map(int, numbers)))
    combinations = []
    for number in numbers:
        combinations += list(number + numbers)
    return combinations


if __name__ == '__main__':
    with open('inputs/day_9.txt', 'r') as file:
        lines = file.readlines()
    lines = list(map(str.strip, lines))

    invalid_number = None
    for line_index in range(preamble_length, len(lines)):
        valid_numbers = find_combinations(lines[line_index-preamble_length:line_index])
        number = lines[line_index]
        if int(number) not in valid_numbers:
            invalid_number = int(number)
            break
    print(f'answer for part one: {invalid_number}')

    indices = None
    for i, number in enumerate(lines):
        done = False
        sum = int(number)
        for j in range(i+1, len(lines)):
            sum += int(lines[j])
            if sum == invalid_number:
                indices = (i, j)
                done = True
                break
        if done:
            break

    (i, j) = indices
    contiguous_range = lines[i:j+1]
    contiguous_range = list(map(int, contiguous_range))
    print(f'Answer to part two: {min(contiguous_range) + max(contiguous_range)}')

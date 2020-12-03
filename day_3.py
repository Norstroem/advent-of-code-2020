import functools
import numpy as np
from typing import Tuple

with open('inputs/day_3.txt', 'r') as file:
    lines = file.readlines()

lines = list(map(str.strip, lines))
horizontal_range = len(lines[0])-1
vertical_range = len(lines)


def horizontal_location(x: int) -> int:
    if x > horizontal_range:
        x = x % (horizontal_range + 1)
    return x


def is_tree(vertical_coordinate: int, horizontal_coordinate: int) -> bool:
    character = lines[vertical_coordinate][horizontal_location(horizontal_coordinate)]
    return character == '#'


def find_trees(slope: Tuple[int, int]) -> int:
    (right, down) = slope

    vertical_coordinates = np.linspace(0, vertical_range-1, round(vertical_range/down))
    vertical_coordinates = list(map(int, vertical_coordinates))

    horizotal_coordinates = np.linspace(0, right/down*(vertical_range-1), round(vertical_range/down))
    horizotal_coordinates = list(map(int, horizotal_coordinates))

    found_trees = list(map(is_tree, vertical_coordinates, horizotal_coordinates))
    return sum(found_trees)


if __name__ == '__main__':
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_list = list(map(find_trees, slopes))

    answer = functools.reduce(lambda x, y: x*y, tree_list)

    print(f'Answer to part one: {tree_list[1]}')
    print(f'Answer to part two: {answer}')

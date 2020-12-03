import functools
import numpy as np

max_horizontal = 30


def horizontal_location(x: int) -> int:
    if x > max_horizontal:
        x = x % (max_horizontal + 1)
    return x


if __name__ == '__main__':
    with open('inputs/day_3.txt', 'r') as file:
        lines = file.readlines()

    lines = list(map(str.strip, lines))
    vertical_range = len(lines)
    tree_list = []
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        (right, down) = slope
        vertical_coordinates = np.linspace(0, vertical_range-1, round(vertical_range/down))
        vertical_coordinates = list(map(int, vertical_coordinates))
        horizotal_coordinates = np.linspace(0, right/down*(vertical_range-1), round(vertical_range/down))
        horizotal_coordinates = list(map(int, horizotal_coordinates))

        trees = 0
        for i, vertical_coordinate in enumerate(vertical_coordinates):
            if lines[vertical_coordinate][horizontal_location(horizotal_coordinates[i])] == '#':
                trees += 1
        tree_list.append(trees)

    answer = functools.reduce(lambda x, y: x*y, tree_list)

    print(f'Answer to part one: {tree_list[1]}')
    print(f'Answer to part two: {answer}')

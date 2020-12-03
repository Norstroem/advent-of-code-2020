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
    vertical_coordinates = np.linspace(0, vertical_range-1, vertical_range)
    vertical_coordinates = list(map(int, vertical_coordinates))
    horizotal_coordinates = np.linspace(0, 3*(vertical_range-1), vertical_range)
    horizotal_coordinates = list(map(int, horizotal_coordinates))

    trees = 0
    for vertical_coordinate in vertical_coordinates:
        if lines[vertical_coordinate][horizontal_location(horizotal_coordinates[vertical_coordinate])] == '#':
            trees += 1

    print(trees)

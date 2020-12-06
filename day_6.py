from functools import reduce
from typing import List


def flatten(str1: str, str2: str) -> str:
    if str2.strip() == '':
        separator = '|'
    else:
        separator = ''
    return f'{str1.strip()}{separator}{str2.strip()}'


def flatten2(str1: str, str2: str) -> str:
    if str2.strip() == '':
        separator = '|'
    else:
        separator = ' '
    return f'{str1.strip()}{separator}{str2.strip()}'


def intersection(sets: List[set]) -> set:
    return reduce(lambda x, y: x.intersection(y), sets)


if __name__ == '__main__':
    with open('inputs/day_6.txt', 'r') as file:
        lines = file.readlines()
    answers = reduce(flatten, lines)
    group_answers = answers.split('|')
    answer_sets = map(set, group_answers)
    yes_answers = list(map(len, answer_sets))
    print(f'Answer to part one: {sum(yes_answers)}')

    answers2 = reduce(flatten2, lines)
    group_answers = answers2.split('|')
    group_answers = map(lambda x: x.strip().split(' '), group_answers)
    group_answers_sets = map(lambda x: map(set, x), group_answers)
    intersections = map(intersection, group_answers_sets)
    yes_answers = map(len, intersections)
    print(f'Answer to part two: {sum(yes_answers)}')

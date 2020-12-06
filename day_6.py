from functools import reduce


def flatten(str1: str, str2: str) -> str:
    if str2.strip() == '':
        separator = '|'
    else:
        separator = ''
    return f'{str1.strip()}{separator}{str2.strip()}'


if __name__ == '__main__':
    with open('inputs/day_6.txt', 'r') as file:
        lines = file.readlines()
    answers = reduce(flatten, lines)
    group_answers = answers.split('|')
    answer_sets = map(set, group_answers)
    yes_answers = list(map(len, answer_sets))
    print(f'Answer to part one: {sum(yes_answers)}')

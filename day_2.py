import multiprocessing as mp
from typing import Tuple


def extract_password(line: str) -> str:
    line = line.strip()
    [_, password] = line.split(':')
    return password


def extract_policy(line: str) -> Tuple[str, int, int]:
    line = line.strip()
    [policy, _] = line.split(':')
    [policy_integers, policy_character] = policy.split(' ')
    [policy_integer_one, policy_integer_two] = policy_integers.split('-')
    return policy_character, int(policy_integer_one), int(policy_integer_two)


def match_character(character: str, reference_character: str) -> bool:
    return character == reference_character


def verify_policy_one(password: str, policy: Tuple[str, int, int]) -> bool:
    (policy_character, min_count, max_count) = policy
    matching_characters = list(map(match_character, list(password), [policy_character]*len(password)))
    return int(min_count) <= sum(matching_characters) <= int(max_count)


def verify_policy_two(password: str, policy: Tuple[str, int, int]) -> bool:
    (policy_character, index_one, index_two) = policy
    first_index_matching = password[index_one] == policy_character
    second_index_matching = password[index_two] == policy_character
    return first_index_matching != second_index_matching


if __name__ == '__main__':
    pool = mp.Pool()

    with open('inputs/day_2.txt', 'r') as file:
        lines = file.readlines()
    passwords = pool.starmap(extract_password, zip(lines))
    policies = pool.starmap(extract_policy, zip(lines))

    approved_passwords = pool.starmap(verify_policy_one, zip(passwords, policies))
    print(f'Valid number of passwords for part one: {sum(approved_passwords)}')

    approved_passwords = pool.starmap(verify_policy_two, zip(passwords, policies))
    print(f'Valid number of passwords for part two: {sum(approved_passwords)}')

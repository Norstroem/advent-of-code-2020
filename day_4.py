import re
from typing import Dict, List, Tuple
from functools import reduce

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def flatten(str1: str, str2: str) -> str:
    if str2.strip() == '':
        separator = '|'
    else:
        separator = ' '
    return f'{str1.strip()}{separator}{str2.strip()}'


def flatten_list_to_dict(dicts: List[Dict]) -> Dict:
    return reduce(lambda x, y: {**x, **y}, dicts)


def exctract_key_value_pair(field: str) -> Dict[str, str]:
    [key, value] = field.split(':')
    return {key: value}


def extract_passports(string: str) -> List[Dict[str, str]]:
    fields = string.split(' ')
    return list(map(exctract_key_value_pair, fields))


def validate_field(key_value: Tuple[str, str]) -> bool:
    (key, value) = key_value
    valid = False

    if key == 'byr':  # Birth Year
        value = int(value)
        valid = value in range(1920, 2003)
    elif key == 'iyr':  # Issue Year
        value = int(value)
        valid = value in range(2010, 2021)
    elif key == 'eyr':  # Expiration Year
        value = int(value)
        valid = value in range(2020, 2031)
    elif key == 'hgt':  # Height
        match = re.match(r"([0-9]+):?(cm|in)", value)
        if match:
            matching_characters = match.span()[1]
            if matching_characters == len(value):
                (height, unit) = match.groups()
                if unit == 'cm':
                    valid = int(height) in range(150, 194)
                elif unit == 'in':
                    valid = int(height) in range(59, 77)
    elif key == 'hcl':  # Hair Color
        if value[0] == '#' and len(value) == 7:
            matching_characters = re.match(r"(?:[a-z]|[0-9])+", value[1:7]).span()[1]
            if matching_characters == 6:
                valid = True
    elif key == 'ecl':  # Eye Color
        valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':  # Passport ID
        try:
            int(value)
            valid = len(value) == 9
        except:
            pass
    elif key == 'cid':  # Country ID
        valid = True

    return valid


def validate_fields(passport: Dict) -> bool:
    valid_fields = list(map(validate_field, list(passport.items())))
    return bool(reduce(lambda x, y: x*y, valid_fields))


def validate_mandatory_fields(passport: Dict) -> bool:
    return set(mandatory_fields).issubset(passport.keys())


def validate_both(bool1: bool, bool2: bool) -> bool:
    return bool1 and bool2


if __name__ == '__main__':
    with open('inputs/day_4.txt', 'r') as file:
        lines = file.readlines()
    flattened_passports = reduce(flatten, lines)
    passport_strings = flattened_passports.split('| ')
    passports = list(map(extract_passports, passport_strings))
    passports = list(map(flatten_list_to_dict, passports))

    contains_mandatory_fields = list(map(validate_mandatory_fields, passports))
    print(f'Part one answer: {sum(contains_mandatory_fields)}')
    fields_valid = list(map(validate_fields, passports))
    all_valid = list(map(validate_both, contains_mandatory_fields, fields_valid))
    print(f'Part two answer: {sum(all_valid)}')

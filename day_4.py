from typing import List

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']


def extract_keys(field: str) -> str:
    key = field.split(':')
    return key[0]


def extract_fields(line: str) -> List[str]:
    fields = line.split(' ')
    return fields


if __name__ == '__main__':
    with open('inputs/day_4.txt', 'r') as file:
        lines = file.readlines()
    lines = list(map(str.strip, lines))

    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_fields = ['cid']

    passports = [[]]
    passport_index = 0
    for line in lines:
        fields = extract_fields(line)
        keys = list(map(extract_keys, fields))
        if keys == ['']:
            passports.append([])
            passport_index += 1
        else:
            passports[passport_index] += keys

    valid_count = 0
    for passport in passports:
        if set(mandatory_fields).issubset(passport):
            valid_count += 1

    print(valid_count)

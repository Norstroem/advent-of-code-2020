import re

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate_field(key: str, value: str) -> bool:
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


if __name__ == '__main__':
    with open('inputs/day_4.txt', 'r') as file:
        lines = file.readlines()
    lines = list(map(str.strip, lines))

    passports_data = [[]]
    passport_index = 0
    for line in lines:
        if line == '':
            passports_data.append([])
            passport_index += 1
        else:
            passports_data[passport_index].append(line)

    passports = []
    for i, passport_data in enumerate(passports_data):
        passports.append({})
        for data_line in passport_data:
            pairs = data_line.split(' ')
            for pair in pairs:
                (key, value) = pair.split(':')
                passports[i][key] = value

    contains_fields_count = 0
    valid_count = 0
    for passport in passports:
        fields_valid = True
        contains_mandatory_fields = set(mandatory_fields).issubset(passport.keys())
        for (key, value) in passport.items():
            if not validate_field(key, value):
                fields_valid = False

        if contains_mandatory_fields:
            contains_fields_count += 1
        if contains_mandatory_fields and fields_valid:
            valid_count += 1
    print(f'Part one answer: {contains_fields_count}')
    print(f'Part two answer: {valid_count}')

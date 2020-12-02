with open('inputs/day_2.txt', 'r') as file:
    lines = file.readlines()

# Part one

valid_count = 0
for line in lines:
    string = line.strip()

    policy = string.split(':')[0]
    password = string.split(':')[1]

    policy_character = policy.split(' ')[1]
    policy_count = policy.split(' ')[0]

    policy_count_min = int(policy_count.split('-')[0])
    policy_count_max = int(policy_count.split('-')[1])

    character_count = 0
    for character in password:
        if character == policy_character:
            character_count += 1

    if character_count >= policy_count_min and character_count <= policy_count_max:
        valid_count += 1

print(f'Valid number of passwords for part one: {valid_count}')


valid_count = 0
for line in lines:
    string = line.strip()

    policy = string.split(':')[0]
    password = string.split(':')[1]

    policy_character = policy.split(' ')[1]
    policy_indices = policy.split(' ')[0]

    policy_first_index = int(policy_indices.split('-')[0])
    policy_second_index = int(policy_indices.split('-')[1])

    first_index_matching = False
    second_index_matching = False

    character_count = 0
    for i, character in enumerate(password):
        if i == policy_first_index and character == policy_character:
            first_index_matching = True
        elif i == policy_second_index and character == policy_character:
            second_index_matching = True

    if first_index_matching != second_index_matching:
        valid_count += 1

print(f'Valid number of passwords for part two: {valid_count}')
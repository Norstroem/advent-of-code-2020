if __name__ == '__main__':
    with open('inputs/day_5.txt', 'r') as file:
        lines = file.readlines()
    boarding_passes = map(str.strip, lines)

    input_string = 'FBLR'
    translation_string = '0101'
    translation = str.maketrans(input_string, translation_string)
    boarding_passes_binary = list(map(lambda x: x.translate(translation), boarding_passes))

    row_range = 7
    rows_binary = map(lambda x: x[0:row_range], boarding_passes_binary)
    columns_binary = map(lambda x: x[row_range:], boarding_passes_binary)

    rows = map(lambda x: int(x, 2), rows_binary)
    columns = map(lambda x: int(x, 2), columns_binary)

    seat_ids = list(map(lambda x, y: 8*x + y, rows, columns))
    missing_seat_id = list(set(range(min(seat_ids), max(seat_ids) + 1)) - set(seat_ids))[0]

    print(f'Answer to part one: {max(seat_ids)}')
    print(f'Answer to part two: {missing_seat_id}')

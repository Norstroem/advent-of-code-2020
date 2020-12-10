if __name__ == '__main__':
    with open('inputs/day_10.txt', 'r') as file:
        lines = file.readlines()
    lines = list(map(str.strip, lines))
    adapter_ratings = list(map(int, lines))
    adapter_ratings = sorted(adapter_ratings)
    adapter_ratings = [0] + adapter_ratings + [adapter_ratings[-1]+3]

    outlet_rating = 0

    diff1 = 0
    diff3 = 0
    for adapter_rating in adapter_ratings:
        difference = adapter_rating - outlet_rating
        if difference == 1:
            diff1 += 1
        elif difference == 3:
            diff3 += 1
        outlet_rating = adapter_rating

    print(f'Answer to part one: {diff1*diff3}')

    arrangements = [1] + [0]*adapter_ratings[-1]
    for i in adapter_ratings[1:]:
        arrangements[i] = arrangements[i-3] + arrangements[i-2] + arrangements[i-1]

    print(f'Answer to part two: {arrangements[-1]}')

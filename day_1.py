import pandas as pd
import numpy as np
import multiprocessing as mp
import functools

input = 'inputs/day_1.txt'

df = pd.read_csv(input, '\n')
entries = df.iloc[:,0]

def add_to_entries(x):
    return x+entries

def add_to_entries2(x):
    return map(add_to_entries, x)

def search_for_match(x):
    result = np.where(x == 2020)
    if result[0].size > 0:
        index = result[0][0]
        return index

def search_for_match2(x):
    return list(map(search_for_match, x))

if __name__ == '__main__':
    pool = mp.Pool()

    # Part one
    added_lists = pool.starmap(add_to_entries, zip(entries))
    indices = np.array(pool.starmap(search_for_match, zip(added_lists)))
    filtered_indices = (indices[pd.notnull(indices)])
    filtered_entries = entries[filtered_indices]
    answer = functools.reduce(lambda x, y: x*y, filtered_entries)
    print(f'Answer to part one: {answer}')

    # Part two
    added_lists = pool.starmap(add_to_entries2, zip(added_lists))
    indices = np.array(pool.starmap(search_for_match2, zip(added_lists)))
    filtered_indices = indices[pd.notnull(indices)]
    unique_indices = list(set(filtered_indices))
    filtered_entries = entries[unique_indices]
    answer = functools.reduce(lambda x, y: x*y, filtered_entries)
    print(f'Answer to part two: {answer}')

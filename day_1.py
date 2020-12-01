import pandas as pd
import numpy as np

input = 'inputs/day_1.txt'

df = pd.read_csv(input, '\n')
entries = df.iloc[:,0]

# part one

for i in range(0, len(entries)):
    rolled_entries = np.roll(entries, i)
    result = np.where(entries + rolled_entries == 2020)
    if result[0].size > 0:
        index = result[0][0]
        answer = rolled_entries[index]*entries[index]
        print(f'Answer to part one: {answer}')
        break

#part two

found_solution = False
for i in range(0, len(entries)):
    rolled = np.roll(entries, i)
    for j in range(0, len(entries)):
        rolled2 = np.roll(entries, j)
        result = np.where(entries + rolled + rolled2 == 2020)
        if result[0].size > 0:
            index = result[0][0]
            answer = rolled[index]*entries[index]*rolled2[index]
            found_solution = True
            print(f'Answer to part two: {answer}')
            break
    if found_solution:
        break


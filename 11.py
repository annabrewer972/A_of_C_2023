import itertools as it

with open ('inputs/input_11.txt', 'r') as f:
    rows = [[char for char in line.strip()] for line in f.readlines()]

# just to save me typing them out later :)
row_len = len(rows[0])
col_len = len(rows)

# find rows that expand
expanding_rows = []
for i in range(col_len):
    if all(x == '.' for x in rows[i]):
        expanding_rows.append(i)

# find cols that expand
expanding_cols = []
for i in range(row_len):
    if all(row[i] == '.' for row in rows):
        expanding_cols.append(i) 

# find galaxies
all_galaxies = []
for j in range(col_len): # iter through rows
    all_galaxies.extend([(j, i) for i in range(row_len) if rows[j][i] == '#'])


expansion_factors = [1, 999999] # for each 'expanding' row/column, you get *this* many extra rows/columns...

def find_dist(gal_1, gal_2, exp_factor): # finds distance between two galaxies using the manhattan distance, including any additional rows/columns due to 'expansion'... 
    x = sorted([gal_1[0], gal_2[0]])
    y = sorted([gal_1[1], gal_2[1]])
    additional_rows = len([thing for thing in expanding_rows if x[0] < thing < x[1]]) * exp_factor
    additional_cols = len([thing for thing in expanding_cols if y[0] < thing < y[1]]) * exp_factor
    x_dist = x[1] - x[0] + additional_rows
    y_dist = y[1] - y[0] + additional_cols
    dist = x_dist + y_dist
    return dist

answers = []

for i, my_factor in enumerate(expansion_factors): # for part 1 then part 2
    tot_dist = 0
    for my_gal_1, my_gal_2 in it.combinations(all_galaxies, 2): # all possible pair combos
        tot_dist += find_dist(my_gal_1, my_gal_2, my_factor)
    answers.append(tot_dist)
    print(f'answer to part {i+1}: {tot_dist}')

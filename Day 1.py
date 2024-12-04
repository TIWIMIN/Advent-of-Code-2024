from collections import defaultdict

column_1 = list()
column_2 = list()

file = open("Day 1 input.txt", "r")
for line in file: 
    values = line.strip().split()
    column_1.append(int(values[0]))
    column_2.append(int(values[1]))

column_1.sort()
column_2.sort()

diff = 0

for i in range(len(column_1)): 
    diff += abs(column_1[i] - column_2[i])

print("diff:", diff)

# part 2

hash_map = defaultdict(lambda: 0)
sim_score = 0

for i in range(len(column_2)): 
    hash_map[column_2[i]] += 1

for i in range(len(column_1)): 
    sim_score += column_1[i] * hash_map[column_1[i]]

print("sim_score:", sim_score)
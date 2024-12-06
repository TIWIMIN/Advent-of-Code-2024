from collections import defaultdict
from functools import cmp_to_key

file = open("input.txt", "r")
    
top_section = list()
bottom_section = list()
is_bottom_section = False

for line in file: 
    line = line.strip()
    if not line: 
        continue
    
    if ',' in line: 
        is_bottom_section = True
    
    if is_bottom_section: 
        bottom_section.append(line)
    else: 
        top_section.append(line)

hash_map = defaultdict(set)
mid_sum = 0
incorrect_lines = list()

for line in top_section: 
    a, b = map(int, (line.split('|')))
    hash_map[a].add(b)

for line in bottom_section: 
    line = list(map(int,line.split(',')))
    valid = True
    for i in range(len(line)): 
        for j in range(i + 1, len(line)):
            if line[j] not in hash_map[line[i]]: 
                valid = False
                break
    if valid: 
        mid = (len(line) - 1) // 2
        mid_sum += line[mid]
    if not valid: 
        incorrect_lines.append(line)

print(mid_sum)


incorrect_mid_sum = 0
def custom_comparator (a, b): 
    if b in hash_map[a]:
        return -1
    elif a in hash_map[b]:
        return 1
    else: 
        return 0

for line in incorrect_lines: 
    sorted_line = sorted(line, key = cmp_to_key(custom_comparator))
    mid = (len(line) - 1) // 2
    incorrect_mid_sum += sorted_line[mid]

print(incorrect_mid_sum)

file.close()
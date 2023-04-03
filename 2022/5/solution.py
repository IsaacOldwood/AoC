import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
lines = []
inst = []
append_inst = False

with open(dir_path + '/input.txt') as file:
    for l in file:
        line = l.strip()
        if line == '':
            append_inst = True
        else:
            if append_inst:
                inst.append(line)
            else:
                lines.append(line.split(' '))

# Build initial crate stacks
lines.pop(len(lines) - 1)

for row in lines:
    for idx, i in enumerate(row):
        if i == '':
            row[idx] = '#'
            row.pop(idx+1)
            row.pop(idx+1)
            row.pop(idx+1)
        else:
            row[idx] = i[1]

max_len = len(lines[len(lines)-1])

for row in lines:
    if len(row) < max_len:
        row.extend(['#']*(max_len-len(row)))

stack_dict = {i:[] for i in range (1,max_len + 1)}
for row in lines:
    for idx, i in enumerate(row):
        if i != '#':
            stack_dict[idx + 1].append(i)

# Build instructions
for idx, row in enumerate(inst):
    new_inst = []
    for i in row.split(' '):
        try:
            new_inst.append(int(i))
        except:
            pass
    inst[idx] = new_inst

# Move stacks
for row in inst:
    for _ in range(0, row[0]):
        crate = stack_dict[row[1]].pop(0)
        stack_dict[row[2]].insert(0, crate)

# Print answer
print(''.join([v[0] if v else '' for v in stack_dict.values()]))
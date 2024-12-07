import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + '/input.txt') as file:
    lines = [l.strip() for l in file.readlines()]

current_full_dir = '/'
used_memory = {}

# Collect info
for l in lines:
    if l.startswith('$ cd'):
        if l == '$ cd ..':
            current_full_dir = '/'.join(current_full_dir.split('/')[:-1])
            if not current_full_dir:
                current_full_dir = '/'
            else:
                current_dir = current_full_dir.split('/')[-1]
        elif l == '$ cd /':
            current_full_dir = '/'
        else:
            current_full_dir = (current_full_dir if current_full_dir != '/' else '') + '/' + l.split(' ')[-1]
    elif l.startswith('$ ls'):
        continue
    elif l.startswith('dir'):
        continue
    else:
        dirs = current_full_dir.split('/')[1:] + ['/'] if current_full_dir != '/' else ['/']
        temp_path = ''
        for d in dirs:
            temp_path += d if d == '/' else ('/' + d)
            try:
                used_memory[temp_path] += int(l.split(' ')[0])
            except KeyError:
                used_memory[temp_path] = int(l.split(' ')[0])

print(used_memory)

# Get solution
sol = 0
for k, m in used_memory.items():
    if m <= 100000:
        sol += m

print(sol)
import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

# Rules are stored as a dictionary to easily find all page numbers a given page needs to be before
rules = defaultdict(list)
updates = []
update_section = False

# Parse input
with open(dir_path + "/input.txt") as file:
    for line in file:
        # Input is splut into two sections by an empty line
        if line == "\n":
            update_section = True
            continue

        # Build rules dictionary
        if not update_section:
            split_line = line.split("|")
            update_page = int(split_line[0].strip())
            rule_page = int(split_line[1].strip())
            rules[update_page].append(rule_page)
        # Parse page updates
        else:
            update = [int(x) for x in line.strip().split(",")]
            updates.append(update)

# print(rules, updates)
middle_page_total = 0
for update in updates:
    rule_broken = False
    for page_inx, page in enumerate(update):
        rule = rules[page]
        # Check if any of the rules are violated
        for i in range(0, page_inx):
            val = update[i]
            if val in rule:
                rule_broken = True
                break

        if rule_broken:
            break
    if not rule_broken:
        # Add middle value to total
        middle_page_total += update[len(update) // 2]

print(f"Part 1: {middle_page_total=}")

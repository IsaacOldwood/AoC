import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + "/input.txt") as file:
    lines = [line.rstrip() for line in file]
corrupted_memory = "".join(lines)

# Find valid instructions
instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", corrupted_memory)

total = 0
mul_enabled = True
# Clean and convert to pairs of numbers
for instruction in instructions:
    if instruction == "do()":
        mul_enabled = True
        continue
    elif instruction == "don't()":
        mul_enabled = False
        continue

    if mul_enabled:
        # Remove everything other than numbers
        instruction = instruction.replace("mul(", "").replace(")", "")

        # Split LHS and RHS
        numbers = instruction.split(",")

        # Convert to integers and multiply
        total += int(numbers[0]) * int(numbers[1])

print(f"Part 1: {total=}")  # 189527826
print(f"Part 2: {total=}")  # 63013756

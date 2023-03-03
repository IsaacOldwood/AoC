import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + '/input.txt') as file:
    lines = [line.rstrip() for line in file]

highest_calorie = 0
current_elf_calorie = 0
for cal in lines:
    if cal == '':
        if current_elf_calorie > highest_calorie:
            highest_calorie = current_elf_calorie
        current_elf_calorie = 0
    else:
        current_elf_calorie += int(cal)

print(highest_calorie)

# Part 2
with open(dir_path + '/input.txt') as file:
    lines = [line.rstrip() for line in file]

highest_calorie = 0
second_highest_calorie = 0
third_highest_calorie = 0
current_elf_calorie = 0
for cal in lines:
    if cal == '':
        if current_elf_calorie > highest_calorie:
            third_highest_calorie = second_highest_calorie
            second_highest_calorie = highest_calorie
            highest_calorie = current_elf_calorie
        elif current_elf_calorie > second_highest_calorie:
            third_highest_calorie = second_highest_calorie
            second_highest_calorie = current_elf_calorie
        elif current_elf_calorie > third_highest_calorie:
            third_highest_calorie = current_elf_calorie
        current_elf_calorie = 0
    else:
        current_elf_calorie += int(cal)

print(highest_calorie + second_highest_calorie + third_highest_calorie)
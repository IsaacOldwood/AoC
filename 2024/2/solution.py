import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + "/input.txt") as file:
    reports = [line.rstrip() for line in file]

safe_reports = 0
for report in reports:
    # Split report into list of levels
    levels = [int(x) for x in report.split()]
    current_level = levels[0]

    decreasing = False
    increasing = False
    report_safe = True

    for n in range(1, len(levels)):
        next_level = levels[n]

        # Must increase or decrease by 1
        if next_level == current_level:
            report_safe = False
            break

        diff = next_level - current_level

        # Must increase or decrease by less than 4
        if abs(diff) > 3:
            report_safe = False
            break

        # Must be all increasing or all decreasing
        if diff > 0:
            increasing = True
        elif diff < 0:
            decreasing = True

        if increasing and decreasing:
            report_safe = False
            break

        # Move to next level
        current_level = next_level

    # If all conditions are met, the report is safe
    if report_safe:
        safe_reports += 1

print(f"Part 1: {safe_reports=}")

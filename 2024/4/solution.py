import os
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/input.txt") as file:
    grid = [[c.strip() for c in line.strip()] for line in file]


# Part 1
def get_neighbours(grid, x, y):
    """Get the surrounding neighbours of a cell"""
    neighbours = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Handle edges
            if i == -1 and x == 0:
                continue
            elif i > 0 and x == len(grid) - 1:
                continue
            elif j == -1 and y == 0:
                continue
            elif j > 0 and y == len(grid) - 1:
                continue

            try:
                neighbours[i + 1][j + 1] = grid[x + i][y + j]
            except IndexError:
                pass
    return neighbours


word_count = 0
for row_id, row in enumerate(grid):
    for cell_id, cell in enumerate(row):
        # If not an X then skip
        if cell != "X":
            continue

        # Save x coords for comparison
        x_row_id = row_id
        x_cell_id = cell_id
        # Get cell neighbours
        neighbours = get_neighbours(grid, x_row_id, x_cell_id)
        # print("\n".join([str(row) for row in neighbours]))

        # Iterate over neighbours and find M
        for i, row in enumerate(neighbours):
            for j, cell in enumerate(row):
                if cell != "M":
                    continue

                # Get M coords from relative position
                relative_row = i - 1
                relative_cell = j - 1
                m_row_id = x_row_id + relative_row
                m_cell_id = x_cell_id + relative_cell

                # Get possible A and S coords
                a_row_id = m_row_id + relative_row
                a_cell_id = m_cell_id + relative_cell

                s_row_id = a_row_id + relative_row
                s_cell_id = a_cell_id + relative_cell

                try:
                    # Handle edges
                    if a_row_id < 0 or a_cell_id < 0:
                        continue
                    elif s_row_id < 0 or s_cell_id < 0:
                        continue
                    elif a_row_id >= len(grid) or a_cell_id >= len(grid):
                        continue
                    elif s_row_id >= len(grid) or s_cell_id >= len(grid):
                        continue

                    a = grid[a_row_id][a_cell_id]
                    s = grid[s_row_id][s_cell_id]
                    if a == "A" and s == "S":
                        word_count += 1
                except IndexError:
                    continue

print(f"Part 1: {word_count=}")  # 2514


# Part 2
def get_neighbours(grid, x, y):
    """Get the surrounding neighbours of a cell"""
    neighbours = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Only care about corners
            if i == -1 and j == 0:
                continue
            elif i == 0 and j == -1:
                continue
            elif i == 0 and j == 1:
                continue
            elif i == 1 and j == 0:
                continue

            # Handle edges
            if i == -1 and x == 0:
                continue
            elif i > 0 and x == len(grid) - 1:
                continue
            elif j == -1 and y == 0:
                continue
            elif j > 0 and y == len(grid) - 1:
                continue

            try:
                neighbours[i + 1][j + 1] = grid[x + i][y + j]
            except IndexError:
                pass
    return neighbours


x_mas_count = 0
for row_id, row in enumerate(grid):
    for cell_id, cell in enumerate(row):
        # If not an A then skip
        if cell != "A":
            continue

        # Save a coords for comparison
        a_row_id = row_id
        a_cell_id = cell_id
        # Get cell neighbours
        neighbours = get_neighbours(grid, a_row_id, a_cell_id)
        # print("\n".join([str(row) for row in neighbours]))

        # Check neighbours contain 2 M and 2 S
        neighbour_count = Counter([cell for row in neighbours for cell in row])

        # If not 2 of each then skip
        if neighbour_count["M"] != 2 or neighbour_count["S"] != 2:
            continue

        # Check if M and S are in the correct positions
        # Only need to check two opposite corners
        top_left_corner = neighbours[0][0]
        bottom_right_corner = neighbours[2][2]

        if top_left_corner == bottom_right_corner:
            continue

        # print(f"Found A at {a_row_id=}, {a_cell_id=}")
        x_mas_count += 1

print(f"Part 2: {x_mas_count=}")  # 1888

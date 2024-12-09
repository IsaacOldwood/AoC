import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1
with open(dir_path + "/input.txt") as file:
    grid = [[c.strip() for c in line.strip()] for line in file]


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


# print('\n'.join([str(row) for row in get_neighbours(grid, 9, 0)]))
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

print(f"Part 1: {word_count=}") # 2514

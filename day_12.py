from pathlib import Path
from string import ascii_letters
from typing import Optional

hills, start_pos, end_pos = [], (0, 0), (0, 0)
for row, line in enumerate(Path("data/day_12.txt").read_text().split("\n")):
    current_line = []
    for col, char in enumerate(list(line)):
        if char == "S":  # not strictly required, but it's still nice
            start_pos = (col, row)
            current_line.append(ascii_letters.index("a"))
        elif char == "E":
            end_pos = (col, row)
            current_line.append(ascii_letters.index("z"))
        else:
            current_line.append(ascii_letters.index(char))
    hills.append(current_line)


# %% Question 1:

def breadth_first_search(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> Optional[int]:
    queue = [(0, start)]  # nsteps is recorded along with the next index
    seen = {start}
    nrows = len(grid)
    ncols = len(grid[0])
    while queue:
        steps, path = queue.pop(0)
        x, y = path
        if (x, y) == end:
            return steps
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):  # look up, down, left, right
            if (x2, y2) not in seen and 0 <= x2 < ncols and 0 <= y2 < nrows and grid[y2][x2] <= grid[y][x] + 1:
                queue.append((steps + 1, (x2, y2)))
                seen.add((x2, y2))


breadth_first_search(hills, start_pos, end_pos)

# %% Question 2
distances = []
for y_axis, row in enumerate(hills):
    for x_axis, col in enumerate(row):
        if col != 0:
            continue
        distance = breadth_first_search(hills, (x_axis, y_axis), end_pos)
        if distance is not None:
            distances.append(distance)

min(distances)

from pathlib import Path

# %% Load data
trees = [list(line) for line in Path("data/day_08.txt").read_text().split("\n")]

# %% Question 1: how many trees are visible?
nrows, ncols = len(trees), len(trees[0])


def is_visible(tree_row: int, tree_col: int, grid: list[list[int]]) -> bool:
    current_tree = grid[tree_row][tree_col]
    top_visible = all([grid[row][tree_col] < current_tree for row in range(0, tree_row)])
    bottom_visible = all([grid[row][tree_col] < current_tree for row in range(tree_row + 1, len(trees))])
    left_visible = all([grid[tree_row][col] < current_tree for col in range(0, tree_col)])
    right_visible = all([grid[tree_row][col] < current_tree for col in range(tree_col + 1, len(trees[0]))])
    return top_visible or bottom_visible or left_visible or right_visible


visible = [is_visible(row, col, trees) for col in range(1, ncols - 1) for row in range(1, nrows - 1)]
sum(visible) + 2 * nrows + 2 * ncols - 4  # top, bottom, left, right rows, minus the 4 that overlap


# %% Question 2: calculate scenic score

def count_visible_trees(array: list[int], max_height: int, direction_iterator) -> int:
    count = 0
    for i in direction_iterator:
        count += 1
        if array[i] >= max_height:
            break
    return count


def scenic_score(row: int, col: int, grid, transposed_grid) -> int:
    current_tree = grid[row][col]
    top = count_visible_trees(transposed_grid[col], current_tree, range(row - 1, -1, -1))
    bottom = count_visible_trees(transposed_grid[col], current_tree, range(row + 1, len(grid)))
    left = count_visible_trees(grid[row], current_tree, range(col - 1, -1, -1))
    right = count_visible_trees(grid[row], current_tree, range(col + 1, len(grid[row])))
    return top * bottom * left * right


transposed_trees = list(zip(*trees))  # just to make sure we don't have to calculate this on every function call
scores = [scenic_score(r, c, trees, transposed_trees) for c in range(0, ncols) for r in range(0, nrows)]
max(scores)

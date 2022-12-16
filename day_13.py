from ast import literal_eval
from pathlib import Path

# %% Read and parse data
pairs = [[literal_eval(el) for el in pair.split("\n")] for pair in Path("data/day_13.txt").read_text().split("\n\n")]


def compare(left: list, right: list) -> bool | None:
    for i in range(max(len(left), len(right))):
        if i == len(left):
            return True
        elif i == len(right):
            return False
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] != right[i]:
                return left[i] < right[i]
        else:
            result = compare(left[i] if isinstance(left[i], list) else [left[i]],
                             right[i] if isinstance(right[i], list) else [right[i]])
            if result is not None:
                return result


# %% Question 1: try 2
sum([idx + 1 for idx, (part1, part2) in enumerate(pairs) if compare(part1, part2)])

# %% Question 2:
index1 = sum([compare(item, [[2]]) for pair in pairs for item in pair]) + 1
index2 = sum([compare(item, [[6]]) for pair in pairs for item in pair]) + 2  # [[2]] is also in the list
index1 * index2

from pathlib import Path

data = Path("data/day_04.txt").read_text()
boundaries = [[[int(n) for n in elf.split("-")] for elf in pair.split(",")] for pair in data.split("\n")]

# %% Question 1: check which sets fully overlap
sum([a[0] <= b[0] <= b[1] <= a[1] or b[0] <= a[0] <= a[1] <= b[1] for a, b in boundaries])

# %% Question 2: check which sets overlap at all
sum([a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1] for a, b in boundaries])

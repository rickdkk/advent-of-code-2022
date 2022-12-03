from pathlib import Path

# Read and parse the data, sum of items per elf
cal_counts = [sum([int(item) for item in elf.split("\n")]) for elf in Path("data/day_01.txt").read_text().split("\n\n")]

# %% Question 1: Elf with the highest amount of items
max(cal_counts)

# %% Question 2: Total sum for the top three elves
sum(sorted(cal_counts)[-3:])

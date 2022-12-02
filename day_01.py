from pathlib import Path

# Read and parse the data, list of items per elf
cal_counts = [[int(item) for item in elf.split("\n")] for elf in Path("data/day_01.txt").read_text().split("\n\n")]

# Elf with the highest amount of items
max([sum(elf) for elf in cal_counts])

# Total sum for the top three elves
sum(sorted([sum(elf) for elf in cal_counts])[-3:])

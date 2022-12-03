from pathlib import Path
from string import ascii_letters

# %% Read and parse data
sacks = Path("data/day_03.txt").read_text().split("\n")

# %% Question 1: find matching items between compartments in sacks and calculate score
priorities = []
for sack in sacks:
    first_compartment, second_compartment = sack[:len(sack) // 2], sack[len(sack) // 2:]
    priorities.append([item for item in first_compartment if item in second_compartment])

sum([ascii_letters.index(item[0]) + 1 for item in priorities])  # only use first occurrence

# %% Question 2: find matching items for every three group of elves to determine badge
badges = [[item for item in sacks[i] if item in sacks[i + 1] and item in sacks[i + 2]] for i in range(0, len(sacks), 3)]

sum([ascii_letters.index(badge[0]) + 1 for badge in badges])

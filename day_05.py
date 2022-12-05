import re
from copy import deepcopy
from pathlib import Path

# %% Load and parse data
data = Path("data/day_05.txt").read_text()

to_remove = ["[", "]", "move ", "from ", "to "]
state, instructions = re.sub('|'.join(map(re.escape, to_remove)), "", data).split("\n\n")

state = state.replace("    ", " ").split("\n")[-2::-1]  # invert list and remove redundant column numbering
original_stacks = [list([crate for crate in stack if crate]) for stack in list(zip(*[s.split(" ") for s in state]))]

instructions = [[int(num) for num in line.split(" ")] for line in instructions.split("\n")]  # [amount, origin, dest]

# %% Question 1: what are the letters of the top crates after following all instructions
stacks = deepcopy(original_stacks)  # keep the original original_stacks for reference
for amount, origin, dest in instructions:
    stacks[dest - 1].extend([stacks[origin - 1].pop() for _ in range(amount)])  # use pop to remove from top

"".join(stack[-1] for stack in stacks)

# %% Question 2: what are the letters of the top crates after moving all crates with the CrateMover 9001
stacks = deepcopy(original_stacks)
for amount, origin, dest in instructions:
    stacks[dest - 1].extend(reversed([stacks[origin - 1].pop() for _ in range(amount)]))  # This is just lazy, I know...

"".join(stack[-1] for stack in stacks)

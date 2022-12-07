import re
from pathlib import Path

# %% Read data
input_data = Path("data/day_07.txt").read_text()

# %% Question 1: find the size of all dirs


def execute_instructions(instructions) -> list[int]:
    all_dirs = []
    instructions = iter(instructions.split("\n"))

    def sum_directories() -> int:
        current_dir = 0
        while True:
            next_instruction = next(instructions, "Stop")
            if match := re.findall(r"\d+", next_instruction):
                current_dir += int(match[0])
            elif "cd" in next_instruction and not next_instruction.endswith(".."):
                current_dir += sum_directories()
            elif "cd .." in next_instruction or next_instruction == "Stop":
                all_dirs.append(current_dir)
                return current_dir

    sum_directories()
    return all_dirs


directories = execute_instructions(input_data)
sum([directory for directory in directories if directory <= 100_000])

# %% Question 2
total_space = 70_000_000
required_space = 30_000_000
to_delete = required_space - (total_space - directories[-1])

for directory in sorted(directories):
    if directory >= to_delete:
        print(directory)
        break

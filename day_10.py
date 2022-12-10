from pathlib import Path

# %% Read and parse data
instructions = Path("data/day_10.txt").read_text().split("\n")

# %% Question 1: determine the signal strength after CPU instructions
register, cycles = 1, 0
signal_strength: list[int] = []


def compare_and_append_signal(cycle, value, signals: list[int]):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signals.append(cycle * value)  # inplace modification of signals


for instruction in instructions:
    cycles += 1
    compare_and_append_signal(cycles, register, signal_strength)

    if "addx" in instruction:
        cycles += 1
        compare_and_append_signal(cycles, register, signal_strength)
        register += int(instruction.split(" ")[-1])

sum(signal_strength)

# %% Question 2: simulate the CRT and draw the sprite
CRT = []
cycles, sprite_position, screen_size = 0, 1, 40


def draw_pixel(screen, position, npixels, sprite_size=3):
    current_position = len(screen) % npixels
    sprite_positions = [idx + position - 1 for idx in range(sprite_size)]
    screen.append("#" if current_position in sprite_positions else " ")  # modify inplace


for instruction in instructions:
    cycles += 1  # Start cycle
    draw_pixel(CRT, sprite_position, screen_size)  # End of cycle n

    if "addx" in instruction:
        cycles += 1  # Start of cycle n + 1
        draw_pixel(CRT, sprite_position, screen_size)  # During cycle n + 1
        sprite_position += int(instruction.split(" ")[-1])  # End of cycle n + 1

for i in range(0, len(CRT), screen_size):
    print("".join(CRT[i:i + screen_size]))

from pathlib import Path

# %% Read data
characters = Path("data/day_06.txt").read_text()

# %% Question 1 and 2: Find first series of four and fourteen unique characters
for key_length in (4, 14):
    current_items = []
    for idx, character in enumerate(characters):
        if character in current_items:
            current_items = current_items[current_items.index(character) + 1:]  # 'reset' from the duplicate onward

        current_items.append(character)

        if len(current_items) == key_length:
            print(idx + 1)
            break

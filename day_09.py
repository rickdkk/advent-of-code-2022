from pathlib import Path

# %% Load and parse data
data = "".join([line[0] * int(line[2:]) for line in Path("data/day_09.txt").read_text().split("\n")])

# %% Question 1 and 2: number of locations that the tail has visited for a 2 and 10 length snake


def execute_moves(snake_length: int, moves: str):
    snake = [{"x": 0, "y": 0} for _ in range(snake_length)]
    directions = {"R": ("x", 1), "L": ("x", -1), "U": ("y", 1), "D": ("y", -1)}  # axis, effect mapping
    visited = set()

    for move in moves:
        axis, trans = directions[move]
        snake[0][axis] += trans  # move the head
        for segment in range(1, snake_length):
            dx = snake[segment - 1]["x"] - snake[segment]["x"]
            dy = snake[segment - 1]["y"] - snake[segment]["y"]
            if dx ** 2 + dy ** 2 > 2:
                snake[segment]["x"] += max(-1, min(1, dx))
                snake[segment]["y"] += max(-1, min(1, dy))

        visited.add((snake[-1]["x"], snake[-1]["y"]))
    return len(visited)


print(execute_moves(2, data), execute_moves(10, data))

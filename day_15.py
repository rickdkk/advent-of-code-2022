import re
from pathlib import Path

# %% Read and parse data
sensors = [list(map(int, re.findall(r"-?\d+", line))) for line in Path("data/day_15.txt").read_text().split("\n")]


def distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


ranges = [distance((x1, y1), (x2, y2)) for x1, y1, x2, y2 in sensors]  # distance between sensor and beacon

# %% Question 1: In the row where y=2000000, how many positions cannot contain a beacon?
illegal_positions = set()
row_of_interest = 2_000_000


def illegal_row_positions(row: int, sensor_position, sensor_range) -> set:
    positions = set()
    distance_to_row = abs(sensor_position[1] - row)
    if distance_to_row > sensor_range:
        return positions
    positions.add(sensor_position[0])
    for idx in range(sensor_range - distance_to_row + 1):
        positions.add(sensor_position[0] - idx)
        positions.add(sensor_position[0] + idx)
    return positions


for sensor, srange in zip(sensors, ranges):
    illegal_positions |= illegal_row_positions(row_of_interest, sensor, srange)

for x1, y1, x2, y2 in sensors:  # Remove coords that are already filled with a sensor or beacon
    if y1 == row_of_interest and x1 in illegal_positions:
        illegal_positions.remove(x1)
    if y2 == row_of_interest and x2 in illegal_positions:
        illegal_positions.remove(x2)

len(illegal_positions)

# %% Question 2: Find the only possible position for the distress beacon. What is its tuning frequency?
boundaries = (0, 4_000_000)


def scan_boundaries(all_sensors, all_ranges, max_value):
    found = False
    for current_sensor, sensor_range in zip(all_sensors, all_ranges):
        sensor_x, sensor_y = current_sensor[:2]
        for direction in range(4):  # scan the boundary of the sensor range in 4 half-circles
            for i in range(sensor_range + 1):
                if direction == 0:  # right-upper side
                    cx = sensor_x + sensor_range + 1 - i
                    cy = sensor_y + i
                elif direction == 1:  # left-upper side
                    cx = sensor_x - i
                    cy = sensor_y + sensor_range + 1 - i
                elif direction == 2:  # left-lower side
                    cx = sensor_x - sensor_range - 1 + i
                    cy = sensor_y - i
                else:  # right-lower side
                    cx = sensor_x + i
                    cy = sensor_y - sensor_range - 1 + i
                if 0 <= cx <= max_value and 0 <= cy <= max_value:
                    found = all(distance((cx, cy), sens) > dist for sens, dist in zip(all_sensors, all_ranges))
                if found:
                    return cx, cy


x, y = scan_boundaries(sensors, ranges, boundaries[1])
x * 4_000_000 + y

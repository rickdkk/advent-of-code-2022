from copy import deepcopy
from dataclasses import dataclass
from math import lcm
from pathlib import Path


@dataclass()
class Monkey:
    items: list[int]
    operation: str
    test: int
    true_monkey: int
    false_monkey: int
    bored_rate: int = 3
    inspected_items: int = 0

    def inspect_items(self, monkeys: list["Monkey"], worry_reduction: int = 0):
        true_items = []
        false_items = []
        for item in self.items:
            self.inspected_items += 1
            item = self._inspect_item(item, worry_reduction)
            if item % self.test == 0:
                true_items.append(item)
            else:
                false_items.append(item)
        self.items = []
        self._throw_items(true_items, self.true_monkey, monkeys)
        self._throw_items(false_items, self.false_monkey, monkeys)

    def _inspect_item(self, old: int, worry_reduction: int):
        if worry_reduction:
            return eval(self.operation) % worry_reduction
        else:
            return eval(self.operation) // self.bored_rate

    @staticmethod
    def _throw_items(items: list[int], to: int, monkeys):
        monkeys[to].items.extend(items)


# %% Read and parse data
data = Path("data/day_11.txt").read_text().split("\n\n")

all_monkeys = []
for monkey in data:
    current = monkey.split("\n")
    all_monkeys.append(Monkey([int(num) for num in current[1].split(": ")[-1].split(",")],
                              current[2].split("= ")[-1],
                              int(current[3].split(" ")[-1]),
                              int(current[4].split(" ")[-1]),
                              int(current[5].split(" ")[-1])))

# %% Question 1:
monkeys_1 = deepcopy(all_monkeys)
for _ in range(20):
    for monkey in all_monkeys:
        monkey.inspect_items(all_monkeys)

sorted_monkeys = sorted(all_monkeys, key=lambda m: m.inspected_items, reverse=True)
print(sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items)

# %% Question 2:
least_common_multiple = lcm(*[monkey.test for monkey in all_monkeys])

monkeys_2 = deepcopy(all_monkeys)
for _ in range(10_000):
    for monkey in all_monkeys:
        monkey.inspect_items(all_monkeys, least_common_multiple)

sorted_monkeys = sorted(all_monkeys, key=lambda m: m.inspected_items, reverse=True)
print(sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items)

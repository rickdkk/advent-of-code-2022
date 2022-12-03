from pathlib import Path

ENCODING = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}

ENCODING_GAME2 = {"X": {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"},  # player has to lose
                  "Y": {"Rock": "Rock", "Paper": "Paper", "Scissors": "Scissors"},  # draw, maps elf to player move
                  "Z": {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}}  # win

GAME = {"Rock": {"Rock": 4, "Paper": 1, "Scissors": 7},  # Player plays rock, opponent plays rock/paper/scissors
        "Paper": {"Rock": 8, "Paper": 5, "Scissors": 2},  # Win is 6 points, draw is 3 points, lose is 0 points
        "Scissors": {"Rock": 3, "Paper": 9, "Scissors": 6}}  # Rock is 1 point, paper is 2 points, scissors is 3 points

# Read and parse data
games = [move.split(" ") for move in Path("data/day_02.txt").read_text().split("\n")]  # ["C X", "C Y", "B X", ...]

# Game 1: execute moves according to the game description and look up score
sum([GAME[ENCODING[player]][ENCODING[elf]] for elf, player in games])

# Game 2: act according to win/draw/loss instruction, find correct move, then look up score
sum([GAME[ENCODING_GAME2[player][ENCODING[elf]]][ENCODING[elf]] for elf, player in games])

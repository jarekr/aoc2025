
import sys
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day4_input.txt"

@dataclass
class RollsMap:
    rolls: list[str]
    rows: int
    cols: int
    neighbors: list[str]

    def __init__(self, rolls: list[str]):
        self.rolls = rolls
        self.rows = len(rolls)
        self.cols = len(rolls[0])
        self.neighbors = [[-1] * self.cols for _ in range(self.rows)]

    def scan_and_remove(self) -> int:
        toberemoved = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.rolls[r][c] == '@':
                    if self.access_check(r,c):
                        toberemoved.append((r,c))
        for r, c in toberemoved:
            self.remove_roll(r,c)
        return len(toberemoved)

    def access_check(self, row, col) -> bool:
        count = 0
        for roff, coff in (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST):
            arow, acol = row + roff, col + coff
            if arow >= 0 and arow < self.rows and acol >= 0 and acol < self.cols:
                if self.rolls[arow][acol] == '@':
                    count += 1
        if self.neighbors[row][col] == -1:
            self.neighbors[row][col] = count

        return count < 4

    def remove_roll(self, row, col) -> None:
        self.rolls[row][col] = '.'
        for roff, coff in (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST):
            arow, acol = row + roff, col + coff
            if arow >= 0 and arow < self.rows and acol >= 0 and acol < self.cols:
                if self.rolls[arow][acol] == '@':
                    self.neighbors[arow][acol] -= 1

NORTH = (-1, 0)
NORTH_EAST = (-1, 1)
EAST = (0, 1)
SOUTH_EAST = (1, 1)
SOUTH = (1, 0)
SOUTH_WEST = (1, -1)
WEST = (0, -1)
NORTH_WEST = (-1, -1)

def can_access_roll(row: int, col: int, rmap: RollsMap) -> bool:
    count = 0
    for roff, coff in (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST):
        arow, acol = row + roff, col + coff
        if arow >= 0 and arow < rmap.rows and acol >= 0 and acol < rmap.cols:
            if rmap.rolls[arow][acol] == '@':
                count += 1

    return count < 4

def part1(rolls):
    count = 0
    accessible = 0
    rows = len(rolls)
    cols = len(rolls[0])
    rmap = RollsMap(rolls=rolls, rows=rows, cols=cols)

    for row in range(rows):
        for col in range(cols):
            if rolls[row][col] == '@':
                count += 1
                if can_access_roll(row, col, rmap):
                    accessible += 1

    #import pdb;pdb.set_trace()
    print(f"final {count} rolls, accessible={accessible}")

def part2(rmap: RollsMap):
    total_removed = 0
    rounds = 1
    count = rmap.scan_and_remove()
    while count > 0:
        total_removed += count
        rounds += 1
        count = rmap.scan_and_remove()
    print(f"{rounds=} {total_removed=}")


def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    rolls: list[str] = []
    with open(input_path, "r") as fh:
        for line in fh:
            rolls.append(list(line.strip()))

    if not rolls:
        print(f"failed to find rolls from {input_path}")
        sys.exit(3)

    # part1(rolls)
    part2(RollsMap(rolls))

main()
if __name__ == "__MAIN__":
    main()
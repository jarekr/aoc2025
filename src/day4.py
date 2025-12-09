
import sys
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day4_input.txt"

@dataclass
class RollsMap:
    rolls: list[str]
    rows: int
    cols: int

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

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    rolls: list[str] = []
    with open(input_path, "r") as fh:
        for line in fh:
            rolls.append(line.strip())

    if not rolls:
        print(f"failed to find rolls from {input_path}")
        sys.exit(3)

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
    print(f"{count=}")

    print(f"final {count} rolls, accessible={accessible}")

main()
if __name__ == "__MAIN__":
    main()
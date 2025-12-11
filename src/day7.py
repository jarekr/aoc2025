
import sys
import math
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day7_input.txt"
TESTINPUT_PATH = "inputs/day7_testinput.txt"

# 0: 0, 0 -> 1 # 0
# 1: 1, 1 -> 2 # 1
# 2: 2, 2 -> 3 # 1.5
# 3: 3, 3 -> 4 # 1
# 4: 3, 4 -> 6 # 2
# 5: 4, 6 -> 7 # 1
# 6: 3, 7 -> 9 # 2
# 7: 6, 9 -> 9 # 0

# 0: 0, 0 -> 1 # 1
# 1: 1, 1 -> 2 # 2
# 2: 2, 2 -> 3 # 4
# 3: 3, 3 -> 4 # 7
# 4: 3, 4 -> 6 # 8
# 5: 4, 6 -> 7 # 1
# 6: 3, 7 -> 9 # 2
# 7: 6, 9 -> 9 # 0

def part1(diagram: list[str]):
    if not diagram:
        return
    rows = len(diagram)
    cols = len(diagram[0])
    beam_locs = [0] * cols
    for i in range(cols):
        if diagram[0][i] == 'S':
            beam_locs[i] = 1
            break
    splitcount = 0
    for row in range(1, rows):
        for col in range(cols):
            if diagram[row][col] == '^' and beam_locs[col]:
                splitcount += 1
                beam_locs[col] = 0
                for new_col in (col - 1, col + 1):
                    if new_col >= 0 and new_col < cols and diagram[row][new_col] == '.':
                        beam_locs[new_col] = 1
    print(f"result: {sum(beam_locs)} total beams, {splitcount=}")

@dataclass
class Timeline:
    id: int
    row: int
    col: int


def part2(diagram: list[str]):
    if not diagram:
        return
    rows = len(diagram)
    cols = len(diagram[0])

    tls = [0] * cols

    for i in range(cols):
        if diagram[0][i] == 'S':
            tls[i] = 1
            break

    for row in range(1, rows):
        new_tls = [0] * cols

        for col in range(cols):
            if diagram[row][col] == '.':
                continue
            if diagram[row][col] == '^':
                tlcount = tls[col]
                if not tlcount:
                    continue

                for new_col in (col - 1, col + 1):
                    if new_col >= 0 and new_col < cols and diagram[row][new_col] != '^':
                        new_tls[new_col] += tlcount

                tls[col] = 0

        for i in range(cols):
            tls[i] += new_tls[i]

        tlcount, beams = sum(tls), sum((1 for tls in tls if tls))
        print(f"{row=} {beams=} {tlcount=}")

    tlcount, beams = sum(tls), sum((1 for tls in tls if tls))
    print(f"result: {beams} total beams, {tlcount=}")

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        if sys.argv[1].startswith('-t'):
            input_path = TESTINPUT_PATH
        else:
            input_path = Path(sys.argv[1])

    diagram = []

    with open(input_path, "r") as fh:
        for line in fh:
            diagram.append(line.strip('\n\r'))

    if not diagram:
        print(f"failed to find read diagram from {input_path}")
        sys.exit(3)

    #part1(diagram)
    part2(diagram)


main()
if __name__ == "__MAIN__":
    main()

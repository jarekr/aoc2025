
import sys
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day6_input.txt"

def part1(matrix: list[list[int]]):
    #import pdb;pdb.set_trace()
    rows = len(matrix) - 1
    cols = len(matrix[0])

    values = [int(x) for x in matrix[0]]

    for col in range(cols):
        opstr = matrix[-1][col]
        for row in range(1, rows):
            if opstr == '+':
                values[col] = values[col] + int(matrix[row][col])
            else:
                values[col] = values[col] * int(matrix[row][col])
    print(f"final sum {sum(values)}")

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    matrix = []

    with open(input_path, "r") as fh:
        for line in fh:
            cols = line.strip().split()
            matrix.append(cols)

    if not matrix:
        print(f"failed to find read matrix / ops from {input_path}")
        sys.exit(3)

    print(f"got {len(matrix) - 1} rows and {len(matrix[0])} columns")
    part1(matrix)

    #part2(fresh_ranges, available_ids)

main()
if __name__ == "__MAIN__":
    main()

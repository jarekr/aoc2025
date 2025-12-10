
import sys
import math
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day6_input.txt"

def part1(matrix: list[list[int]]):
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

def part2(matrix: list[list[int]], ops: list[str]):
    values = []
    joinfuncs = {
        '+': sum,
        '*': math.prod
    }
    for row in range(len(matrix)):
        values.append(joinfuncs[ops[row]](matrix[row]))

    print(f"final sum {sum(values)}")

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    tmp = []

    with open(input_path, "r") as fh:
        for line in fh:
            tmp.append(line.strip('\n\r'))
    rows = len(tmp) - 1
    cols = len(tmp[0])

    matrix = []

    values = []
    for col in range(cols-1,-1,-1):
        accum = []

        for row in range(rows):
            if tmp[row][col] != ' ':
                accum.append(tmp[row][col])

        if not accum: # column separator (all spaces)
            matrix.append(values)
            values = []
            continue

        values.append(int("".join(accum)))

    matrix.append(values)

    operations = tmp[rows].split()
    operations.reverse()

    if not matrix:
        print(f"failed to find read matrix / ops from {input_path}")
        sys.exit(3)

    print(f"got {len(matrix) - 1} rows and {len(matrix[0])} columns")
    #part1(matrix)
    part2(matrix, operations)

main()
if __name__ == "__MAIN__":
    main()

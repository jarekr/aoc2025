
import sys
from pathlib import Path
from dataclasses import dataclass

INPUT_PATH = "inputs/day5_input.txt"

def part1(fresh_ranges, avaialble_ids):
    fresh_count = 0
    for id in avaialble_ids:
        for start, end in fresh_ranges:
            if id >= start and id <= end:
                fresh_count += 1
                break
    print(f"found {fresh_count} fresh IDs out of {len(avaialble_ids)}")

def merge_ranges(fresh_ranges):
    if not fresh_ranges:
        return

    fresh_ranges.sort()
    new_ranges = [list(fresh_ranges[0])]
    #import pdb;pdb.set_trace()

    for i in range(1, len(fresh_ranges)):
        start, end = fresh_ranges[i]
        if start > new_ranges[-1][1]:
            new_ranges.append([start, end])
        else:
            new_ranges[-1][1] = max(end, new_ranges[-1][1])
    return new_ranges

def part2(fresh_ranges, _):
    fresh_count = 0

    n = len(fresh_ranges)
    fresh_ranges = merge_ranges(fresh_ranges)
    print(f"merged {n} into {len(fresh_ranges)}")

    for start, end in fresh_ranges:
        fresh_count += (end - start) + 1
    print(f"found {fresh_count} total fresh IDs")

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    fresh_ranges: list[tuple[int]] = []
    available_ids: list[int] = []

    seen_blank = False
    with open(input_path, "r") as fh:
        for line in fh:
            val = line.strip()
            if not val:
                seen_blank = True
                continue
            if not seen_blank:
                s, e = val.split('-')
                fresh_ranges.append((int(s), int(e)))
            else:
                available_ids.append(int(val))

    if not available_ids or not available_ids:
        print(f"failed to find ranges and/or ids from {input_path}")
        sys.exit(3)

    part2(fresh_ranges, available_ids)

main()
if __name__ == "__MAIN__":
    main()

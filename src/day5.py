
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

    part1(fresh_ranges, available_ids)

main()
if __name__ == "__MAIN__":
    main()

import sys
import math
from pathlib import Path
from dataclasses import dataclass
from heapq import heappush, heappop

INPUT_PATH = "inputs/day8_input.txt"
TESTINPUT_PATH = "inputs/day8_testinput.txt"

def dist(p1, p2):
    return ((p1[0]-p2[0])**2 +
            (p1[1]-p2[1])**2 +
            (p1[2]-p2[2])**2 )

def find_smallest_dist(adjacency: dict) -> tuple:
    # 906,360,560
    heap = []
    for box in adjacency:
        by_dist = sorted(adjacency[box], key=lambda x: sum([(x[i] - box[i])**2 for i in (0,1,2)]))
        adjacency[box] = by_dist
        #print(f"{box}: {(adjacency[box])}")
        heappush(heap, (by_dist[0], box))
    shortest = heappop(heap)
    return shortest


def part1(boxes: list[tuple[int]]):
    #print(f"result: {sum(beam_locs)} total beams, {splitcount=}")
    # 1. build adjacency list of edges for each point
    starting_box = boxes[0]
    adjacency = {}
    for box in boxes:
        for subbox in boxes:
            if box == subbox:
                continue
            adjacency.setdefault(box, set()).add(subbox)
            adjacency.setdefault(subbox, set()).add(box)

    print(f"from start {starting_box}: {adjacency[starting_box]}")

    shortest = find_smallest_dist(adjacency)
    print(f"shortest dist=={shortest}")

    print(f"{len(boxes)} boxes {len(adjacency)} adj keys")

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        if sys.argv[1].startswith('-t'):
            input_path = TESTINPUT_PATH
        else:
            input_path = Path(sys.argv[1])

    boxes = []

    with open(input_path, "r") as fh:
        for line in fh:
            boxes.append(tuple([int(x) for x in line.strip().split(',')]))

    if not boxes:
        print(f"failed to find read boxes from {input_path}")
        sys.exit(3)

    part1(boxes)


main()
if __name__ == "__MAIN__":
    main()

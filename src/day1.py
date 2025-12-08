
import sys

input_path = "day1_input.txt"

if len(sys.argv) > 1:
    input_path = sys.argv[1]

#import pdb;pdb.set_trace()

def turn_to(pos: int, rot: str) -> int:
    rdir, rdist = rot[0], int(rot[1:])
    zeroes_past_count = 0

    if rdir == 'L':
        new_pos = pos - rdist
        if new_pos < 0:
            zeroes_past_count = -1 * (new_pos // 100)
            if pos == 0:
                zeroes_past_count -= 1
        new_pos = new_pos % 100
        if new_pos == 0:
            zeroes_past_count += 1

    else:
        new_pos = pos + rdist
        zeroes_past_count = new_pos // 100
        new_pos = new_pos % 100

    #import pdb;pdb.set_trace()
    print(f"{rot=} {pos=} -> {new_pos=} {zeroes_past_count=}")
    return (new_pos, zeroes_past_count)



directions = []
count = 0
zero_count = 0
pos = 50

with open(input_path, "r") as fh:
    for line in fh:
        count += 1
        old_pos = pos
        pos, zeroes_past_count = turn_to(old_pos, line.strip())
        zero_count += zeroes_past_count

print(f"final pos={pos} after {count} turns, {zero_count=}")



import sys
from pathlib import Path

INPUT_PATH = "inputs/day3_input.txt"

def find_max_joltage(bank: str):
    max_bat , left_max, right_max = -1, -1, -1
    max_bati, left_maxi, right_maxi = -1, -1, -1

    for i, bats in enumerate(bank):
        bat = int(bats)
        if bat > max_bat:
            old_max = max_bat
            old_maxi = max_bati
            max_bat = bat
            max_bati = i
            if old_max > left_max:
                left_max = old_max
                left_maxi = old_maxi
            if right_maxi < max_bati:
                right_maxi = -1
                right_max = -1

        elif bat > right_max:
            right_max = bat
            right_maxi = i
    options = []
    if right_max != -1:
        options.append(int(f"{max_bat}{right_max}"))
    else:
        options.append(int(f"{left_max}{max_bat}"))
    return options[0]

def main():
    input_path = Path(INPUT_PATH)
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    powerbanks: list[str] = []
    import pdb;pdb.set_trace()
    with open(input_path, "r") as fh:
        for line in fh:
            powerbanks.append(line.strip())

    if not powerbanks:
        print(f"failed to find powerbanks from {input_path}")
        sys.exit(3)

    joltages = []

    for bank in powerbanks:
        #print(f"{bank=}")
        joltages.append(find_max_joltage(bank))

    #import pdb;pdb.set_trace()
    print(f"{joltages=}")

    print(f"final {len(joltages)} joltages, sum={sum(joltages)}")

main()
if __name__ == "__MAIN__":
    main()
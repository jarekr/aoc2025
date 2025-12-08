
import sys

input_path = "day2_input.txt"

if len(sys.argv) > 1:
    input_path = sys.argv[1]

def is_valid_id(id: int)->bool:
    idstr = str(id)
    n = len(idstr)
    if n % 2 != 0:
        return True
    midp = n // 2
    return idstr[:midp] != idstr[midp:]

def get_invalid_ids(start_id: str, end_id: str) -> [int]:
    invalid_ids = []
    for id in range(int(start_id), int(end_id)+1):
        if not is_valid_id(id):
            invalid_ids.append(id)
    return invalid_ids

all_id_ranges: str = ""
with open(input_path, "r") as fh:
    all_id_ranges = fh.readline()

if not all_id_ranges:
    print(f"failed to find id ranges from {input_path}")
    sys.exit(3)
all_invalid_ids = []

for id_range in all_id_ranges.strip().split(','):
    if not id_range:
        continue
    print(f"{id_range=}")
    #if id_range.startswith("95"):
    #    import pdb;pdb.set_trace()
    start_id, end_id = id_range.split('-')
    all_invalid_ids.extend(get_invalid_ids(start_id, end_id))

#import pdb;pdb.set_trace()
#print("..")

print(f"final {len(all_invalid_ids)} invalid ids, sum={sum(all_invalid_ids)}")

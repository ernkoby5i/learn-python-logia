# https://adventofcode.com/2025/day/1
# python
from pathlib import Path
import re

from jupyter_client.session import new_id

PATH = Path("./advent-of-code-2025-d1-e1-szyfr.txt")
#PATH = Path("./advent-of-code-2025-d1-e1-szyfr_test.txt")

def parse_file(path: Path) -> list[tuple[str, int]]:
    """Read file, find tokens like R12 or L234 and return list of tuples."""
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    szyfr: list[tuple[str, int]] = []
    pattern = re.compile(r'\b([RL])\s*(\d+)\b', re.I)
    for line in lines:
        for d, n in pattern.findall(line):
            szyfr.append((d.upper(), int(n)))
    return szyfr

def puzzle_1(start_pos, max_pos, szyfr):
    pos = start_pos
    zero_count = 0
    i = 0
    for direction, steps in szyfr:
        i = i+1
        new_pos = pos
        if direction == 'R':
            new_pos = new_pos + steps
            new_pos = new_pos % (max_pos + 1)
        elif direction == 'L':
            steps2 = steps % (max_pos + 1)
            new_pos = new_pos - steps2
            if new_pos <0:
                new_pos = new_pos + (max_pos + 1)
        if new_pos == 0:
            zero_count = zero_count + 1
        print(f"{i} pos={pos} krok =({direction}, {steps}) new_pos={new_pos} zero_count={zero_count}")
        pos = new_pos


    print(f"Final pos={pos}, zero_count={zero_count}")
    return zero_count

def puzzle_2(start_pos,  max_pos, szyfr):
    pos = start_pos
    zero_count = 0

    move = 0
    max_steps = max_pos + 1
    for direction, steps in szyfr:
        move = move + 1

        if direction == 'R':
            steps_to_do = steps
            print(f"{move=} R:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count} START")
            while steps_to_do >= max_steps:
                zero_count = zero_count + 1
                steps_to_do = steps_to_do - max_steps
                print(f"{move=} R:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count}")
            if steps_to_do > 0:
                start_pos = pos
                pos = pos + steps_to_do
                steps_to_do = 0
                if pos > max_pos:
                    pos = pos - (max_pos + 1)
                    if start_pos != 0:
                        zero_count = zero_count + 1
            print(f"{move=} R:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count} STOP at {pos}")
            continue

        if direction == 'L':
            steps_to_do = steps
            print(f"{move=} L:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count} START")
            while steps_to_do >= max_steps:
                zero_count = zero_count + 1
                steps_to_do = steps_to_do - max_steps
                print(f"{move=} L:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count}")
            if steps_to_do > 0:
                start_pos = pos
                pos = pos - steps_to_do
                steps_to_do = 0
                if pos == 0:
                    zero_count = zero_count + 1
                if pos < 0:
                    pos = (max_pos + 1) + pos
                    if start_pos != 0:
                        zero_count = zero_count + 1
            print(f"{move=} L:{steps} pos={pos} steps_to_do={steps_to_do} zero_count={zero_count} STOP at {pos}")
            continue

    print(f"Final pos={pos}, zero_count={zero_count}")
    return

if __name__ == "__main__":
    szyfr = parse_file(PATH)
    i = 0
    for t in szyfr:
        i = i+1
        #print(f"{i} krok =", t)

    start = 50
    max = 99


    #p1 = puzle_1(start, max, szyfr)
    p2 = puzzle_2(start, max, szyfr)




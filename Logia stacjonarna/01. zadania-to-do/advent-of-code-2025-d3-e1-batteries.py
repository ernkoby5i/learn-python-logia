# https://adventofcode.com/2025/day/1
# python
from doctest import debug
from pathlib import Path
import re

from jupyter_client.session import new_id

f1 = Path("./advent-of-code-2025-d3-e1-batteries-test.txt")
f2 = Path("./advent-of-code-2025-d3-e1-batteries-full.txt")

def parse_file(file_path: Path, debug=False) -> list[str]:
    """Read file, find tokens like R12 or L234 and return list of tuples."""
    if not file_path.exists():
        return []
    lines = file_path.read_text(encoding="utf-8").splitlines()
    if debug:
        for bank in lines:
            print(bank)
    print(f"{file_path} Total banks: {len(lines)}")
    return lines

def maxVoltage(bank: str, n=2) -> int:
    batteries = [int(x) for x in list(bank)]
    max_digits = []
    max_positions = []

    digits_found = 0

    for j in range(n):
        max_digit = -1
        start_idx = 0
        if digits_found>0:
            #max_digit = max_digits[digits_found-1]
            start_idx = max_positions[digits_found-1]+1
        pos = start_idx
        for i in range(start_idx, len(batteries)-   (n - digits_found-1)):
            if max_digit<batteries[i]:
                max_digit = batteries[i]
                pos = i
        max_digits.append(max_digit)
        max_positions.append(pos)
        digits_found = digits_found + 1

    _maxVoltage = 0
    i = n
    for d in max_digits:
        _maxVoltage = _maxVoltage + d*10**(i-1)
        i = i - 1

    print(f"Bank: {bank} {n} Max voltages: {max_digits}  Total: {_maxVoltage}")
    return _maxVoltage


def puzzle1(file_path: Path, n, debug=False):
    banks = parse_file(file_path, debug)
    total_voltage = 0
    for bank in banks:
        total_voltage = total_voltage + maxVoltage(bank,n)
    print(f"Total voltage for all banks: {total_voltage}\n")
    return 0



def puzzle2(file_path: Path):
    banks = parse_file(file_path)
    return 0

if __name__ == "__main__":
    puzzle1(f1,12, debug=True)
    puzzle1(f2,12, debug=False)




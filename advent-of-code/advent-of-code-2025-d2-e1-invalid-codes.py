# https://adventofcode.com/2025/day/1
# python
from pathlib import Path
import re


f1 = Path("advent-of-code-2025-d1-e1-invalid-codes-test.txt")
f2 = Path("advent-of-code-2025-d1-e1-invalid-codes-full.txt")


def parse_file(path: Path) -> list[tuple[str, int]]:
    """Read file, find tokens like R12 or L234 and return list of tuples."""
    if not path.exists():
        return []
    line = path.read_text(encoding="utf-8")
    codes =  line.split(',')
    pattern = re.compile(r'(\d+)-(\d+)', re.I)
    delta = 0
    ranges = []
    for code  in codes:
        match = pattern.match(code)
        if match:
            start = int(match.group(1))
            end = int(match.group(2))
            delta = delta + (end - start)
            ranges.append((code, start, end))
            print(f"Code: {code} start={start} end={end} VALID")
        else:
            print(f"Code: {code} INVALID")
    print(f"Total delta of valid codes: {delta}")
    return ranges

def isValid1(number: int) -> bool:
    s = str(number)
    length = len(s)
    if length % 2 != 0:
        return True
    s1=s[0:length//2]
    s2=s[length//2:length]
    if s1 == s2:
        # print(f"{number} first half {s1} != second half {s2}")
        return False
    return

def isValid2(number: int) -> bool:
    s = str(number)
    length = len(s)
    for i in range(1, length):
        if length % i != 0:
            continue
        section = s[0:i]
        if s == section * (length//i):
            return False
    return True

def puzzle1(file_path: Path):
    codes = parse_file(file_path)
    invalid_count = 0
    invalid_sum = 0
    for (code,start,end) in codes:
        productID = start
        while productID <= end:
            if not isValid1(productID):
                invalid_count = invalid_count + 1
                invalid_sum = invalid_sum + productID
            productID = productID + 1
    print(f"File: {file_path} Invalid codes count: {invalid_count} sum: {invalid_sum}\n")
    pass

def puzzle2(file_path: Path):
    codes = parse_file(file_path)
    invalid_count = 0
    invalid_sum = 0
    for (code,start,end) in codes:
        productID = start
        while productID <= end:
            if not isValid2(productID):
                invalid_count = invalid_count + 1
                invalid_sum = invalid_sum + productID
            productID = productID + 1
    print(f"File: {file_path} Invalid codes count: {invalid_count} sum: {invalid_sum}\n")
    pass

if __name__ == "__main__":
    puzzle1(f1)
    puzzle1(f2)
    puzzle2(f1)
    puzzle2(f2)



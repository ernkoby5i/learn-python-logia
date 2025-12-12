# https://adventofcode.com/2025/day/1
# python
from pathlib import Path
import re

PATH = Path("./advent-of-code-2025-d1-e1-szyfr.txt")
PATH = Path("./advent-of-code-2025-d1-e1-szyfr_test.txt")

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

if __name__ == "__main__":
    szyfr = parse_file(PATH)
    i = 0
    for t in szyfr:
        i = i+1
        print(f"{i} krok =", t)

    start = 50
    max = 99
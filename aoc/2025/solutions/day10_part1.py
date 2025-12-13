import re
from itertools import combinations

def solve(data: list[str]) -> int:
    """
    For each line, find the minimum number of buttons needed to XOR to the target pattern.
    Returns the sum of minimum button presses across all lines.
    """
    total = 0
    for line in data:
        target, buttons = parse_line(line)
        presses = min_presses(target, buttons)
        total += presses

    return total

def min_presses(target: int, buttons: list[int]) -> int | None:
    n = len(buttons)
    for i in range(1, n + 1):
        for combo in combinations(buttons, i):
            xor = 0
            for b in combo:
                xor ^= b
            if xor == target:
                return i
    return None

def parse_line(line: str):
    tokens = re.findall(r"(\[.*?]|\(.*?\))", line)
    target_str, button_strs = tokens[0], tokens[1:]

    width = len(target_str) - 2

    target = pattern_to_bits(target_str)
    buttons = [
        button_schematic_to_bits(tuple(map(int, b.strip("()").split(","))), width)
        for b in button_strs
    ]

    return target, buttons

def pattern_to_bits(pattern: str) -> int:
    core = pattern.strip("[]")
    return int(core.replace(".", "0").replace("#", "1"), 2)

def button_schematic_to_bits(schematic: tuple[int, ...], width: int) -> int:
    return sum(1 << (width - 1 - i) for i in schematic)
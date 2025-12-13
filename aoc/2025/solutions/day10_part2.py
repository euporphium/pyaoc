# I credit this: https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

import re
from functools import lru_cache
from itertools import combinations
from .day10_part1 import button_schematic_to_bits


def solve(data: list[str]) -> int:
    """
    Find minimum button presses using a recursive halving strategy.
    Returns the sum across all lines.
    """
    total = 0
    for line in data:
        buttons, target = parse_line(line)
        total += min_presses(target, buttons)
    return total


def parse_line(line: str):
    tokens = re.findall(r"(\(.*?\)|{.*?})", line)
    button_strs, target_str = tokens[:-1], tokens[-1]
    buttons = [tuple(map(int, b.strip("()").split(","))) for b in button_strs]
    target = [int(x) for x in target_str.strip("{}").split(",")]
    return buttons, target


def find_parity_solutions(target_bits: int, buttons: list[int]) -> list[tuple[int, int]]:
    results = []
    for i in range(len(buttons) + 1):
        for combo in combinations(range(len(buttons)), i):
            xor_val = 0
            for idx in combo:
                xor_val ^= buttons[idx]
            if xor_val == target_bits:
                mask = sum(1 << idx for idx in combo)
                results.append((mask, i))
    return results


@lru_cache(None)
def _min_presses_cached(target: tuple[int, ...],
                        button_masks: tuple[int, ...],
                        width: int) -> int:
    if all(v == 0 for v in target):
        return 0

    parity_bits = 0
    for i, val in enumerate(target):
        if val % 2:
            parity_bits |= 1 << (width - 1 - i)

    solutions = find_parity_solutions(parity_bits, list(button_masks))
    if not solutions:
        return 10**6

    best = float("inf")
    for mask, presses in solutions:
        new_target = list(target)
        for idx, btn_mask in enumerate(button_masks):
            if mask & (1 << idx):
                for bitpos in range(width):
                    if btn_mask & (1 << (width - 1 - bitpos)):
                        new_target[bitpos] -= 1
        if any(v < 0 for v in new_target):
            continue
        halved = tuple(v // 2 for v in new_target)
        cost = _min_presses_cached(halved, button_masks, width)
        best = min(best, 2 * cost + presses)
    return best


def min_presses(target: list[int], buttons: list[tuple[int, ...]]) -> int:
    width = len(target)
    masks = [button_schematic_to_bits(b, width) for b in buttons]
    return _min_presses_cached(tuple(target), tuple(masks), width)
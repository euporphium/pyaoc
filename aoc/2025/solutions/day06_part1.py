import math

def solve(data: list[str]) -> int:
    """
    Parse a grid of vertically arranged math problems and compute their results.
    Each column (minus the last symbol row) forms one problem; the bottom cell
    gives the operator (* or +). Adds all problem results for the grand total.
    """

    total = 0

    grid = [line.split() for line in data]
    transpose = list(zip(*grid))

    for col in transpose:
        nums = map(int, col[:-1])
        op = col[-1]
        total += math.prod(nums) if op == "*" else sum(nums)

    return total
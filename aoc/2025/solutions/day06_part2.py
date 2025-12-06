import math

def solve(data: list[str]) -> int:
    """
    Solve the cephalopod right‑to‑left worksheet. Each column of digits forms a
    vertical number, read top‑to‑bottom, and problems are processed right‑to‑left.
    The operator at the column's bottom applies to all numbers seen so far.
    """

    max_width = max(len(line) for line in data)
    padded = [line.ljust(max_width) for line in data]
    transposed = list(zip(*padded))

    total = 0
    current = []
    for col in reversed(transposed):
        raw = ''.join(col[:-1]).strip()

        if not raw:
            continue

        current.append(int(raw))

        op = col[-1]
        if op in ['*', '+']:
            total += math.prod(current) if op == '*' else sum(current)
            current = []

    return total
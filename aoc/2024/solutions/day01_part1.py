def solve(data: list[str]) -> int:
    """
    Pair up each smallest left value with the smallest right value,
    compute absolute differences, and sum them.
    """

    left = []
    right = []

    for line in data:
        if not line.strip():
            continue
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    distance = sum(abs(a - b) for a, b in zip(left, right))
    return distance

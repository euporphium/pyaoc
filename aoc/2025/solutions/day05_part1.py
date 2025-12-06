def solve(data: list[str]) -> int:
    """
    For each available ID, check whether it falls within any fresh range.
    Straightforward O(n × m) approach — fine for small inputs, but not optimal.
    """

    total = 0

    part1, part2 = "\n".join(data).strip().split("\n\n", 1)

    ranges = [tuple(map(int, x.split("-"))) for x in part1.splitlines()]
    available = part2.splitlines()

    for a in available:
        for low, high in ranges:
            if low <= int(a) <= high:
                total += 1
                break

    return total

# NOTE: AI-assisted optimization / structure reference
def solve_better(data: list[str]) -> int:
    """
    Count how many available ingredient IDs are fresh.

    This implementation merges overlapping fresh ID ranges first
    (for efficiency) and then uses binary search for O(n log m) checks
    across the merged, sorted ranges.
    """

    import bisect

    part1, part2 = "\n".join(data).strip().split("\n\n", 1)

    # Parse and merge fresh ranges
    ranges = sorted(
        [tuple(map(int, line.strip().split("-"))) for line in part1.splitlines()],
        key=lambda x: x[0],
    )

    merged = []
    for low, high in ranges:
        if not merged or merged[-1][1] < low - 1:
            merged.append((low, high))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], high))

    # Store just the starts for bisect lookups
    starts = [low for low, _ in merged]

    total = 0
    for raw_id in part2.splitlines():
        val = int(raw_id)
        # Find rightmost range start <= val
        i = bisect.bisect_right(starts, val) - 1
        if i >= 0 and merged[i][0] <= val <= merged[i][1]:
            total += 1

    return total
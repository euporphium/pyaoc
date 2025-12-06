def solve(data: list[str]) -> int:
    """
    Merge overlapping fresh ID ranges and count the total number of unique IDs covered.
    Sorting allows efficient linear merging; overall O(m log m) complexity.
    """

    part1, _ = "\n".join(data).strip().split("\n\n", 1)

    sorted_ranges = sorted(
        [tuple(map(int, line.strip().split("-"))) for line in part1.splitlines()],
        key=lambda x: x[0],
    )

    current_low, current_high = sorted_ranges[0]
    total = 0

    for next_low, next_high in sorted_ranges[1:]:
        if next_low <= current_high:
            current_high = max(current_high, next_high)
        else:
            total += current_high - current_low + 1
            current_low, current_high = next_low, next_high

    total += current_high - current_low + 1

    return total

def solve(data: list[str]) -> int:
    """
    For each numeric range in the input, find all product IDs where the number
    consists of two identical halves. Returns the sum of all such invalid IDs
    across all ranges.
    """

    ranges = data[0].split(",")
    total = 0

    for r in ranges:
        low, high = r.split("-")

        for i in range(int(low), int(high) + 1):
            text = str(i)
            mid = len(text) // 2

            if text[:mid] == text[mid:]:
                total += i

    return total

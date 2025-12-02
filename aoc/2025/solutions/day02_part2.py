def solve(data: list[str]) -> int:
    """
    Find all product IDs that are invalid. An ID is invalid if it consists of
    some sequence of digits repeated at least twice.
    """

    ranges = data[0].split(",")
    total = 0

    for r in ranges:
        low, high = r.split("-")

        for i in range(int(low), int(high) + 1):
            text = str(i)

            if text in (text + text)[1:-1]:
                total += i

    return total

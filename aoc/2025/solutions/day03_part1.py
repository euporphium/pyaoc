def solve(data: list[str]) -> int:
    """
    For each bank of battery joltages, select two digits in order that form the
    largest possible two-digit number. Return the sum of these maximum joltages
    across all banks.
    """

    total = 0

    for line in data:
        first_idx = max(range(len(line) - 1), key=lambda i: int(line[i]))
        first = int(line[first_idx])
        second = max(map(int, line[first_idx + 1:]))

        total += 10 * first + second


    return total

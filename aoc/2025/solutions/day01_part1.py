def solve(data: list[str]) -> int:
    """
    Simulate movement around a 100-position dial starting at 50.
    Return the number of times the position stops at exactly zero.
    """

    position = 50
    times_at_zero = 0

    for line in data:
        direction = line[0]
        distance = int(line[1:])

        position += distance if direction == "R" else -distance
        position %= 100

        if position == 0:
            times_at_zero += 1

    return times_at_zero

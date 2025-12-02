def solve(data: list[str]) -> int:
    """
    Simulate movement around a 100-position dial starting at 50.
    Return the number of times the position passes through or stops at zero.
    """

    position = 50
    times_passing_zero = 0

    for line in data:
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            times_passing_zero += (position + distance) // 100
            position = (position + distance) % 100
        else:
            if position == 0:
                times_passing_zero += distance // 100
            elif distance >= position:
                times_passing_zero += (distance - position) // 100 + 1
            position = (position - distance) % 100

    return times_passing_zero

def solve(data: list[str]) -> int:
    """
    Simulates the downward movement of a tachyon beam through the manifold.
    Each step, the current set of beam positions ('beam') is advanced one row down.
    - Beams continue straight through '.'.
    - When a beam encounters a splitter ('^'), it stops and produces two new beams:
      one immediately to the left and one immediately to the right.

    Returns the total number of times a splitter causes a beam to split.
    """

    beam = {data[0].index('S')}
    splits = 0

    for line in data[1:]:
        next_beam = set()

        for b in beam:
            if line[b] == '^':
                splits += 1

                if b - 1 >= 0:
                    next_beam.add(b - 1)
                if b + 1 < len(line):
                    next_beam.add(b + 1)
            else:
                next_beam.add(b)

        beam = next_beam
    return splits

def solve(data: list[str]) -> int:
    """
    Given the coordinates of red tiles on a grid, find the largest possible
    rectangle that can be formed by choosing any two red tiles as opposite corners.
    The function calculates and returns the maximum area among all such rectangles.
    """

    red_tiles = [tuple(map(int, line.split(','))) for line in data]
    largest_area = 0

    for i, (x1, y1) in enumerate(red_tiles):
        for x2, y2 in red_tiles[i + 1:]:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > largest_area:
                largest_area = area

    return largest_area

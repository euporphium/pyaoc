def solve(data: list[str]) -> int:
    """
    Count how many rolls of paper ('@') have fewer than four neighboring rolls
    (considering all eight surrounding cells).  These are the rolls forklifts can
    initially access.
    """

    total = 0

    row_count = len(data)
    col_count = len(data[0])

    def get_neighbors(r: int, c: int):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < row_count and 0 <= nc < col_count:
                    yield nr, nc

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "@":
                neighbor_count = sum(data[nr][nc] == "@" for nr, nc in get_neighbors(row, col))
                if neighbor_count < 4:
                    total += 1

    return total

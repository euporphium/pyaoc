from collections import deque

def solve(data: list[str]) -> int:
    """
    Iteratively remove rolls of paper ('@') with fewer than four neighbors,
    updating neighbor counts after each removal, until no more can be removed.
    Return the total number of rolls removed.
    """

    total = 0
    row_count = len(data)
    col_count = len(data[0])
    q = deque()
    counts = [[0 for c in range(col_count)] for r in range(row_count)]

    def get_neighbors(r: int, c: int):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < row_count and 0 <= nc < col_count:
                    yield nr, nc

    # Precompute neighbor counts and initial removable cells
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "@":
                neighbor_count = sum(data[nr][nc] == "@" for nr, nc in get_neighbors(row, col))
                counts[row][col] = neighbor_count
                if neighbor_count < 4:
                    q.append((row, col))

    # Remove rolls iteratively
    while q:
        r, c = q.popleft()
        total += 1
        for nr, nc in get_neighbors(r, c):
            if data[nr][nc] != "@":
                continue

            if counts[nr][nc] == 4:
                q.append((nr, nc))

            if counts[nr][nc] > 0:
                counts[nr][nc] -= 1

    return total

from functools import lru_cache

def solve(data: list[str]) -> int:
    """
    Returns the number of distinct timelines resulting from the quantum tachyon
    manifold simulation. Each '^' splits the time stream in two:
    - A particle encountering '^' continues left and right (if in bounds).
    - A '.' just passes the particle straight down.
    A timeline ends when the particle exits the bottom of the manifold.
    """

    rows, cols = len(data), len(data[0])
    start_col = data[0].index("S")

    @lru_cache(maxsize=None)
    def count_timelines(row: int, col: int) -> int:
        if row >= rows:
            return 1

        if col < 0 or col >= cols:
            return 0

        if data[row][col] == "^":
            return count_timelines(row + 1, col - 1) + count_timelines(row + 1, col + 1)

        return count_timelines(row + 1, col)

    return count_timelines(1, start_col)

# NOTE: AI-assisted optimization / structure reference
def solve_bottom_up(data: list[str]) -> int:
    rows, cols = len(data), len(data[0])
    start_col = data[0].index("S")

    # dp[row][col] = number of timelines starting from (row, col)
    # Add an extra row at the bottom for a base case
    dp = [[0] * cols for _ in range(rows + 1)]

    # Base: one successful "timeline" when reaching beyond the bottom
    dp[rows] = [1] * cols  # not used except for reference in row = rows - 1

    # Fill from the bottom-1 up to row 1
    for row in range(rows - 1, 0, -1):
        for col in range(cols):
            if data[row][col] == "^":
                left = dp[row + 1][col - 1] if col - 1 >= 0 else 0
                right = dp[row + 1][col + 1] if col + 1 < cols else 0
                dp[row][col] = left + right
            else:
                dp[row][col] = dp[row + 1][col]  # continue straight

    # Starting point (S is in row 0)
    return dp[1][start_col]
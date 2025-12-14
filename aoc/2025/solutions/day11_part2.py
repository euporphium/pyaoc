from functools import lru_cache

def solve(data: list[str]) -> int:
    """
    Recursively count all paths from 'svr' to 'out' that pass through both 'dac' and 'fft'.
    Uses @lru_cache to memoize intermediate results based on the current node
    and whether 'dac' and 'fft' have been visited so far.
    """

    graph = {}
    for line in data:
        key, right_side = line.split(": ")
        graph[key] = right_side.split()

    @lru_cache(maxsize=None)
    def dfs(node: str, v_dac=False, v_fft=False) -> int:
        if node == 'out' and v_dac and v_fft:
            return 1
        total = 0
        for child in graph.get(node, []):
            total += dfs(child, v_dac or node == 'dac', v_fft or node == 'fft')
        return total

    return dfs('svr')

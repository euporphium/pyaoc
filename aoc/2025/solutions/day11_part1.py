from functools import lru_cache

def solve(data: list[str]) -> int:
    """
    Recursively count all possible paths from 'you' to 'out' by following directed edges.
    Uses @lru_cache to memoize results for each node, avoiding redundant recomputation
    in shared subgraphs and ensuring efficient traversal of the network.
    """

    graph = {}
    for line in data:
        key, right_side = line.split(": ")
        graph[key] = right_side.split()

    @lru_cache(maxsize=None)
    def dfs(node: str) -> int:
        if node == 'out':
            return 1
        total = 0
        for child in graph.get(node, []):
            total += dfs(child)
        return total

    return dfs('you')

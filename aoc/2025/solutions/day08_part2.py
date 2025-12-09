import heapq
import math

def solve(data: list[str]) -> int:
    """
    # Compute all pairwise distances between junction boxes and connect pairs
    # in order of increasing distance until all boxes are in one circuit.
    # Return the product of the X coordinates of the final pair that completes the circuit.
    """

    coords = [tuple(map(int, line.split(","))) for line in data]

    # measure distances between all points
    distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            heapq.heappush(distances, (math.dist(coords[i], coords[j]), (coords[i], coords[j])))

    graph = {c: set() for c in coords}

    def is_connected():
        visited = set()
        start = next(iter(graph))
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node] - visited)
        return len(visited) == len(coords)

    while True:
        _, (a, b) = heapq.heappop(distances)
        graph[a].add(b)
        graph[b].add(a)
        last = (a, b)
        if is_connected():
            break

    a, b = last
    return a[0] * b[0]
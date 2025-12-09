import heapq
import math

def solve(data: list[str]) -> int:
    """
    # Compute distances for all coordinate pairs (brute-force) to find the 1000 shortest links.
    # Build a graph from these connections, then perform DFS to find connected circuits.
    # Return the product of the sizes of the three largest circuits.
    """

    connections = 1000

    coords = [tuple(map(int, line.split(","))) for line in data]

    # measure distances between all points
    distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            heapq.heappush(distances, (math.dist(coords[i], coords[j]), (coords[i], coords[j])))

    # build graph from the shortest distances
    graph = {}
    for i in range(connections):
        _, (a, b) = heapq.heappop(distances)

        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    # ensure every junction box appears, even if unconnected
    for coord in coords:
        graph.setdefault(coord, set())

    # find all circuits in the graph
    visited = set()
    circuits = []
    for node in graph:
        if node not in visited:
            stack = [node]
            current_circuit = []

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    current_circuit.append(current)
                    stack.extend(graph[current] - visited)

            circuits.append(current_circuit)

    circuits.sort(key=len, reverse=True)

    return math.prod(len(c) for c in circuits[:3])
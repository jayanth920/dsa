from collections import defaultdict


def removeStones(stones):
    # # Using DFS + Graph Method
    # # Create a graph using adjacency list
    # graph = defaultdict(list)

    # # Build the graph: connect stones that are in the same row or column
    # for i, (x1, y1) in enumerate(stones):
    #     for j in range(i + 1, len(stones)):
    #         x2, y2 = stones[j]
    #         if x1 == x2 or y1 == y2:
    #             graph[(x1, y1)].append((x2, y2))
    #             graph[(x2, y2)].append((x1, y1))

    # # Set to keep track of visited nodes
    # visited = set()

    # def dfs(stone):
    #     # Use DFS to explore all stones in this connected component
    #     stack = [stone]
    #     visited.add(stone)
    #     while stack:
    #         x, y = stack.pop()
    #         for neighbor in graph[(x, y)]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 stack.append(neighbor)

    # # Count number of connected components
    # num_components = 0
    # for stone in stones:
    #     coord = tuple(stone)
    #     if coord not in visited:
    #         dfs(coord)
    #         num_components += 1

    # # The maximum number of stones that can be removed is the total number of stones
    # # minus the number of connected components
    # return len(stones) - num_components

    # Using UNION FIND
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Helper function to union two nodes
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY  # Union by rank is optional here

    parent = {}  # Dictionary to keep track of parent nodes

    # Initialize the Union-Find structure for each stone
    for x, y in stones:
        # Use row and column indices as part of the union-find structure
        # (x, y) coordinates are mapped to x and ~y to handle rows and columns uniquely
        parent[x] = x
        parent[~y] = (
            ~y
        )  # ~y is used to differentiate columns from rows in the parent map
        union(x, ~y)  # Connect the row and column

    # Count the number of unique connected components
    return len(stones) - len({find(x) for x in parent})

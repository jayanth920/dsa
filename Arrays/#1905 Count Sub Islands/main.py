def countSubIslands(grid1, grid2):
    def dfs(r, c):
        # If out of bounds or at a water cell, return
        if r < 0 or c < 0 or r >= len(grid2) or c >= len(grid2[0]) or grid2[r][c] == 0:
            return True

        # Assume it's a sub-island unless proven otherwise
        is_sub_island = True

        # If the corresponding cell in grid1 is water, it's not a sub-island
        if grid1[r][c] == 0:
            is_sub_island = False

        # Mark the current cell as visited
        grid2[r][c] = 0

        # Explore all four directions
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            is_sub_island &= dfs(r + dr, c + dc)

        return is_sub_island

    sub_island_count = 0

    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if grid2[i][j] == 1 and dfs(i, j):
                # If this island is a sub-island, increment the count
                sub_island_count += 1

    return sub_island_count

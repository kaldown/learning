class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if not rows or not cols:
            return 0

        islands = 0

        def mark_the_island(row, col):
            if 0 <= row < rows and 0 <= col < cols:
                if grid[row][col] != "1":
                    return

                grid[row][col] = "2"

                mark_the_island(row + 1, col)
                mark_the_island(row - 1, col)
                mark_the_island(row, col + 1)
                mark_the_island(row, col - 1)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    islands += 1
                    mark_the_island(x, y)

        return islands

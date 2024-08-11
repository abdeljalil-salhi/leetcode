class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int, visited: Set[Tuple[int, int]]) -> None:
            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            for nrow, ncol in [
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ]:
                dfs(nrow, ncol, visited)

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col, visited)
                    islands += 1

        if islands != 1:
            return 0

        island = list(visited)
        for row, col in island:
            grid[row][col] = 0
            visited = set()
            islands = 0
            for nrow in range(ROWS):
                for ncol in range(COLS):
                    if grid[nrow][ncol] and (nrow, ncol) not in visited:
                        dfs(nrow, ncol, visited)
                        islands += 1
            if islands != 1:
                return 1
            grid[row][col] = 1

        return 2

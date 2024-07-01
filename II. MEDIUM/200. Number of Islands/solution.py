class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row: int, col: int) -> None:
            deq = deque([(row, col)])
            visited.add((row, col))

            while deq:
                r, c = deq.popleft()
                for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + drow, c + dcol
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        deq.append((nr, nc))

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands

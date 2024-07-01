class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = minutes = rotten = 0
        deq = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    deq.append((row, col))
                    rotten += 1

        while deq and fresh:
            for _ in range(rotten):
                r, c = deq.popleft()
                rotten -= 1

                for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + drow, c + dcol
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        deq.append((nr, nc))
                        rotten += 1
                        fresh -= 1

            minutes += 1

        return minutes if not fresh else -1

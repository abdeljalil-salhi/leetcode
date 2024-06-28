class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = deque()
        minutes = fresh = size = 0

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    deq.append((i, j))
                    size += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while deq and fresh:
            for _ in range(size):
                i, j = deq.popleft()
                size -= 1

                for di, dj in directions:
                    row, col = i + di, j + dj
                    if 0 <= row < R and 0 <= col < C and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        deq.append((row, col))
                        size += 1

            minutes += 1

        return minutes if not fresh else -1

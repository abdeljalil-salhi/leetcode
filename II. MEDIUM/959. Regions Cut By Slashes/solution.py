class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        size = N * 3
        pixels = [[0] * size for _ in range(size)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == "/":
                    pixels[r * 3][c * 3 + 2] = 1
                    pixels[r * 3 + 1][c * 3 + 1] = 1
                    pixels[r * 3 + 2][c * 3] = 1
                elif grid[r][c] == "\\":
                    pixels[r * 3][c * 3] = 1
                    pixels[r * 3 + 1][c * 3 + 1] = 1
                    pixels[r * 3 + 2][c * 3 + 2] = 1

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= size or y < 0 or y >= size or pixels[x][y] != 0:
                return
            pixels[x][y] = -1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        regions = 0
        for r in range(size):
            for c in range(size):
                if pixels[r][c] == 0:
                    regions += 1
                    dfs(r, c)

        return regions

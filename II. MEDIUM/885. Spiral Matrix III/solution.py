class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        spiral = []
        row, col = rStart, cStart
        steps = 1
        i = n = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while n < rows * cols:
            for _ in range(2):
                drow, dcol = dirs[i]
                for _ in range(steps):
                    if 0 <= row < rows and 0 <= col < cols:
                        spiral.append([row, col])
                        n += 1
                    row, col = row + drow, col + dcol
                i = (i + 1) % 4
            steps += 1

        return spiral

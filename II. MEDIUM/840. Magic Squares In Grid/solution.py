class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        magic = 0

        def isMagic(row: int, col: int) -> bool:
            hashset = set()
            for i in range(3):
                for j in range(3):
                    hashset.add(grid[row + i][col + j])

            if hashset != set(range(1, 10)):
                return False
            if sum(grid[row][col : col + 3]) != 15:
                return False
            if sum(grid[row + 1][col : col + 3]) != 15:
                return False
            if sum(grid[row + 2][col : col + 3]) != 15:
                return False
            if sum(grid[row + i][col] for i in range(3)) != 15:
                return False
            if sum(grid[row + i][col + 1] for i in range(3)) != 15:
                return False
            if sum(grid[row + i][col + 2] for i in range(3)) != 15:
                return False
            if grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15:
                return False
            if grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15:
                return False
            return True

        for row in range(ROWS - 2):
            for col in range(COLS - 2):
                if grid[row + 1][col + 1] == 5 and isMagic(row, col):
                    magic += 1

        return magic

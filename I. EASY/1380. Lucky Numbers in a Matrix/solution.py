class Solution:
    def luckyNumbers(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        minimum_row = set()
        for row in range(ROWS):
            minimum_row.add(min(grid[row]))

        maximum_col = set()
        for col in range(COLS):
            current_max = grid[0][col]
            for row in range(1, ROWS):
                current_max = max(current_max, grid[row][col])
            maximum_col.add(current_max)

        return [n for n in minimum_row if n in maximum_col]

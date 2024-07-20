class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)
        matrix = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]

        return matrix

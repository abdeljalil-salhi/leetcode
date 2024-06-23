class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def findLargest(i, j) -> int:
            maximum = 0

            # iterate over the 3x3 grid around i, j and find the maximum value
            for x in range(i - 1, i + 2):
                if x < 0 or x >= n:
                    continue
                for y in range(j - 1, j + 2):
                    maximum = max(maximum, grid[x][y])

            return maximum

        n, ans = len(grid), []

        # iterate over the grid and find the largest value for each 3x3 grid
        for i in range(n - 2):
            sub = []
            for j in range(n - 2):
                sub.append(findLargest(i + 1, j + 1))
            ans.append(sub)

        return ans

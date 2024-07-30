class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res, n = 0, len(rating)

        for i in range(n):
            left, right = [0, 0], [0, 0]

            for j in range(i + 1, n):
                if rating[i] > rating[j]:
                    right[0] += 1
                elif rating[i] < rating[j]:
                    right[1] += 1

            for j in range(i):
                if rating[i] > rating[j]:
                    left[0] += 1
                elif rating[i] < rating[j]:
                    left[1] += 1

            res += right[0] * left[1] + right[1] * left[0]

        return res

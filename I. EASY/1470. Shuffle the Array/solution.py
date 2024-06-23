class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y, res = nums[:n], nums[-n:], []

        for i in range(n):
            res.append(x[i]), res.append(y[i])

        return res

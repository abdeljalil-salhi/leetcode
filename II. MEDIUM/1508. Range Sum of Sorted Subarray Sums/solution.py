class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []

        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                res.append(current)

        res.sort()
        return sum(res[left - 1 : right]) % (pow(10, 9) + 7)

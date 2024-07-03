class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n, ans = len(nums), float("inf")

        if n <= 4:
            return 0

        nums.sort()

        for left in range(4):
            right = n - 4 + left
            ans = min(ans, nums[right] - nums[left])

        return ans

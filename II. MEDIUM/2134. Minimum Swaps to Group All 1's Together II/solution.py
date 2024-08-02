class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)
        maximum = current = sum(nums[:total])

        for i in range(n):
            current -= nums[i]
            current += nums[(i + total) % n]
            maximum = max(maximum, current)

        return total - maximum

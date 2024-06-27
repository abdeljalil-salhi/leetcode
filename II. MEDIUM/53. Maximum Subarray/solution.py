class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float("-inf")
        max_ending_here = 0

        # Kadane's Algorithm
        for e in nums:
            max_ending_here += e
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

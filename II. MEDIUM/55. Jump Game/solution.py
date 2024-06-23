class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, maximum = len(nums), 0

        # Iterate through the nums array and find the maximum jump that can be made
        for i in range(n - 1):
            # If the current index is greater than the maximum jump that can be made, return False
            if i > maximum:
                return False

            # Update the maximum jump that can be made
            maximum = max(maximum, i + nums[i])
            # If the maximum jump can reach the end, return True
            if maximum >= n - 1:
                return True

        # Return False if we cannot reach the end
        return False

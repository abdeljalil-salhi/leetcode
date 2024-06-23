class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = jumps = current_max = 0

        # Iterate through the nums array and find the maximum jump that can be made
        for i in range(n - 1):
            maximum = max(maximum, i + nums[i])

            # If the current index is equal to the current maximum, increment the jumps and update the current maximum
            if i >= current_max:
                jumps += 1
                current_max = maximum

        # Return the number of jumps
        return jumps

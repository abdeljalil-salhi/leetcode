class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i, current_range, l = 0, 0, 1, len(nums)

        while current_range <= n:
            # If the current number is less than or equal to the current range
            # Then we can extend the current range to the right by adding the current number
            if i < l and nums[i] <= current_range:
                current_range += nums[i]
                i += 1
            # If the current number is greater than the current range
            # Then we need to add the current range to the count of patches
            # This is because we cannot reach the current number with the current range
            else:
                current_range += current_range
                patches += 1

        return patches

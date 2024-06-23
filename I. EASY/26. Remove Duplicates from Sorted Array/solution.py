class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r, n = 1, len(nums)

        for i in range(1, n):
            # If the current element is not equal to the previous element, then we have a new element
            if nums[i] != nums[i - 1]:
                # Replace the element at index r with the new element
                nums[r] = nums[i]
                r += 1

        # Return the result
        return r

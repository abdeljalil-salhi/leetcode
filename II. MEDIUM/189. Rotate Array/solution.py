class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        # Rotate the array using slicing technique (✨ PYTHONIC ✨) in-place
        nums[:] = nums[-k:] + nums[:-k]

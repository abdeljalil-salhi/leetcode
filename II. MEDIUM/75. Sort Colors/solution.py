class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickSort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            mid = self.partition(nums, low, high)
            self.quickSort(nums, low, mid - 1)
            self.quickSort(nums, mid + 1, high)

    def sortColors(self, nums: List[int]) -> None:
        self.quickSort(nums, 0, len(nums) - 1)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        return sorted(nums, key=lambda num: (freqs[num], -num))

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def getPairs(distance: int) -> int:
            pairs = j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                pairs += j - i - 1
            return pairs

        nums.sort()
        n = len(nums)
        low, high = 0, nums[n - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if getPairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

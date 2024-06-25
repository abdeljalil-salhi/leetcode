class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap, n = {}, len(nums)

        for i in range(n):
            if nums[i] in hmap and abs(i - hmap[nums[i]]) <= k:
                return True
            hmap[nums[i]] = i

        return False

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n, count = len(nums), 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1

        return count

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mymap, n, i = {i: 1 for i in nums}, len(nums), 0

        while i < n:
            if mymap[nums[i]] > 2:
                nums.pop(i)
                n -= 1
            else:
                mymap[nums[i]] += 1
                i += 1

        return len(nums)

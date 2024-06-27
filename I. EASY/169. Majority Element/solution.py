class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hmap = {}

        for e in nums:
            # count the frequency of each element
            if e in hmap:
                hmap[e] += 1
            else:
                hmap[e] = 1
            # check if the element is majority without iterating through the whole list
            if hmap[e] > n / 2:
                return e

        # return the element with the highest frequency if the majority element is not found
        return max(hmap, key=hmap.get)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mymap = {i: 0 for i in nums}

        # Store the frequency of each element in the dictionary
        for i in nums:
            mymap[i] += 1

        # Return the element with the maximum frequency in the dictionary (✨ PYTHONIC ✨)
        return max(mymap, key=mymap.get)

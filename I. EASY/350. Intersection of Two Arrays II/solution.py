class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = Counter()
        ans = []

        for n in nums1:
            hmap[n] += 1

        for n in nums2:
            if n in hmap and hmap[n] > 0:
                ans.append(n)
                hmap[n] -= 1

        return ans

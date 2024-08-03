class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hmap = {}

        for n in target:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1

        for n in arr:
            if n in hmap:
                hmap[n] -= 1
                if hmap[n] == 0:
                    del hmap[n]
            else:
                return False

        return len(hmap) == 0

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}

        for c in magazine:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1

        for c in ransomNote:
            if c in hmap:
                hmap[c] -= 1
                if hmap[c] == -1:
                    return False
            else:
                return False

        return True

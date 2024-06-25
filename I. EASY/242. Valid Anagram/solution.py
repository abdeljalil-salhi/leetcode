class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        # Add all characters' frequencies in s
        for c in s:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1

        # Subtract all characters' frequencies in t
        for c in t:
            if c in hmap:
                hmap[c] -= 1
            else:
                return False

        # Check if all characters' frequencies are 0
        # If not, it means that the strings are not anagrams
        for c in hmap:
            if hmap[c] != 0:
                return False

        # If all characters' frequencies are 0, it means that the strings are anagrams
        return True

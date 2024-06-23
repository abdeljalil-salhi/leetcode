class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        table = {c: i for i, c in enumerate(t)}
        return sum(abs(i - table[c]) for i, c in enumerate(s))

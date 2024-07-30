class Solution:
    def minimumDeletions(self, s: str) -> int:
        minimum = freq = 0

        for c in s:
            if c == "b":
                freq += 1
            elif freq:
                minimum += 1
                freq -= 1

        return minimum

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 if c in jewels else 0 for c in stones)

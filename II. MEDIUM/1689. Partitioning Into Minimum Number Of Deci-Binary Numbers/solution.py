class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0

        for c in n:
            r = ord(c) - ord("0")
            if r > ans:
                ans = r

        return ans

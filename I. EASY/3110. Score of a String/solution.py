class Solution:
    def scoreOfString(self, s: str) -> int:
        n, ans = len(s), 0

        for i in range(n - 1):
            # Use ord() to get the ASCII value of a character
            ans += abs(ord(s[i]) - ord(s[i + 1]))

        return ans

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        n = len(s) // 2
        return all(s[i] == s[~i] for i in range(n))

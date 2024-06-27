class Solution:
    def longestPalindrome(self, s: str) -> int:
        hset = set()
        ans = 0

        # Count the number of characters that appear an odd number of times
        for c in s:
            if c in hset:
                hset.remove(c)
                ans += 2
            else:
                hset.add(c)

        # If there are any characters left in the set, we can use one of them in the middle of the palindrome
        if hset:
            ans += 1

        # Return the length of the longest palindrome
        return ans

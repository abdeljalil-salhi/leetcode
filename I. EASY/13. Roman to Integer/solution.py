class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans, i, n = 0, 0, len(s)

        while i < n:
            if i < n - 1 and table[s[i + 1]] > table[s[i]]:
                ans += table[s[i + 1]] - table[s[i]]
                i += 1
            else:
                ans += table[s[i]]
            i += 1

        return ans

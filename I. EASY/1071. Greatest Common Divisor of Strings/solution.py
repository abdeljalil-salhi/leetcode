class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return a if not b else gcd(b, a % b)

        if str1 + str2 == str2 + str1:
            return str1[: gcd(len(str1), len(str2))]

        return ""

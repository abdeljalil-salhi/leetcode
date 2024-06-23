class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # ✨ MATHEMATICS ✨

        # Fermat's theorem on sums of two squares
        i = 2
        while i * i <= c:
            if c % i == 0:
                exp = 0
                while c % i == 0:
                    exp += 1
                    c //= i
                if i % 4 == 3 and exp % 2:
                    return False
            i += 1
        return c % 4 != 3

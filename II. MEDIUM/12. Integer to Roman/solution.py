class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        integers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        n, ans = 12, ""

        # Greedily subtract the largest possible integer from num
        while num > 0:
            value = num // integers[n]
            num %= integers[n]

            # Append the corresponding roman numeral to the answer
            while value:
                ans += romans[n]
                value -= 1

            n -= 1

        return ans

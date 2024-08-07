class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def counter(n: int) -> str:
            upto_20 = [
                "",
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
                "Ten",
                "Eleven",
                "Twelve",
                "Thirteen",
                "Fourteen",
                "Fifteen",
                "Sixteen",
                "Seventeen",
                "Eighteen",
                "Nineteen",
            ]
            tens = [
                "",
                "",
                "Twenty",
                "Thirty",
                "Forty",
                "Fifty",
                "Sixty",
                "Seventy",
                "Eighty",
                "Ninety",
            ]
            if n < 20:
                return upto_20[n]
            elif n < 100:
                return tens[n // 10] + ("" if n % 10 == 0 else " " + upto_20[n % 10])
            else:
                return (
                    upto_20[n // 100]
                    + " Hundred"
                    + ("" if not n % 100 else " " + counter(n % 100))
                )

        billions = num // 1_000_000_000
        millions = (num // 1_000_000) % 1_000
        thousands = (num // 1_000) % 1_000
        mod = num % 1_000  # mod to keep the rest

        ans = []
        if billions:
            ans.append(counter(billions) + " Billion")
        if millions:
            ans.append(counter(millions) + " Million")
        if thousands:
            ans.append(counter(thousands) + " Thousand")
        if mod:
            ans.append(counter(mod))

        return " ".join(ans)

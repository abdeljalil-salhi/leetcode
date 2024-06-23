class Solution:
    def myAtoi(self, s: str) -> int:
        i, l, n, sn = 0, len(s), 0, 1

        # Skip leading whitespaces
        while i < l and s[i] == " ":
            i += 1

        # Parse the sign of the number if it exists
        if i < l and (s[i] == "-" or s[i] == "+"):
            sn = -1 if s[i] == "-" else 1
            i += 1

        # Parse the number
        while i < l and s[i].isnumeric():
            n = n * 10 + int(s[i])
            i += 1

        # Return the number with the sign and the bounds check applied
        return (
            -2147483648
            if n * sn < -2147483648
            else 2147483647 if n * sn > 2147483647 else n * sn
        )

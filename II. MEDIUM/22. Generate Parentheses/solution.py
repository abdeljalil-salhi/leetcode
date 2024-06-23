class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(current, opened, closed) -> None:
            # If the current string has the desired length, add it to the answer
            # and stop the recursion
            if len(current) == n * 2:
                ans.append(current)
                return

            # Add open parenthesis if there are still open parenthesis left
            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            # Add close parenthesis if there are more open than close parenthesis
            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        ans = []
        # Start the recursion with an empty string and 0 opened and closed parenthesis
        backtrack("", 0, 0)

        return ans

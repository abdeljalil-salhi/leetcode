class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not len(stack) or hmap[c] != stack.pop():
                    return False

        return not len(stack)

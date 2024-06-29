class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def eval(a: int, b: int, sign: str) -> int:
            if sign == "+":
                return a + b
            elif sign == "-":
                return b - a
            elif sign == "*":
                return a * b
            return int(b / a)

        for token in tokens:
            if token in "+-*/":
                stack.append(eval(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))

        return stack[0]

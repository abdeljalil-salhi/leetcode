class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0

        def process_pairs(pair: str, score: int) -> int:
            nonlocal s
            stack, points = [], 0

            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    points += score
                    continue
                stack.append(c)

            s = "".join(stack)

            return points

        if x > y:
            total_points += process_pairs("ab", x)
            total_points += process_pairs("ba", y)
        else:
            total_points += process_pairs("ba", y)
            total_points += process_pairs("ab", x)

        return total_points

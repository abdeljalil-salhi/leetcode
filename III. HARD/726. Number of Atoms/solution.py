class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == "(":
                stack.append({})
            elif formula[i] == ")":
                hashmap = stack.pop()
                multiplier = 0
                while i + 1 < n and formula[i + 1].isdigit():
                    multiplier = multiplier * 10 + int(formula[i + 1])
                    i += 1
                for atom in hashmap:
                    if atom in stack[-1]:
                        stack[-1][atom] += hashmap[atom] * max(multiplier, 1)
                    else:
                        stack[-1][atom] = hashmap[atom] * max(multiplier, 1)
            else:
                element = formula[i]
                while i + 1 < n and formula[i + 1].islower():
                    element += formula[i + 1]
                    i += 1
                multiplier = 0
                while i + 1 < n and formula[i + 1].isdigit():
                    multiplier = multiplier * 10 + int(formula[i + 1])
                    i += 1
                if element in stack[-1]:
                    stack[-1][element] += max(multiplier, 1)
                else:
                    stack[-1][element] = max(multiplier, 1)
            i += 1

        return "".join(
            f"{element}{'' if stack[0][element] == 1 else stack[0][element]}"
            for element in sorted(stack[0])
        )

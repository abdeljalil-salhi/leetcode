class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        combs = []

        def backtrack(current: int, target: int, path: List[int]) -> None:
            if target <= 0:
                if target == 0:
                    combs.append(path.copy())
                return

            for i in range(current, n):
                if i > current and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])

        return combs

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start: int, current: List[int], remaining_target: int) -> None:
            if not remaining_target:
                ans.append(list(current))
                return

            n = len(candidates)
            for i in range(start, n):
                if candidates[i] > remaining_target:
                    break
                current.append(candidates[i])
                backtrack(i, current, remaining_target - candidates[i])
                current.pop()

        candidates.sort()
        ans = []
        backtrack(0, [], target)

        return ans

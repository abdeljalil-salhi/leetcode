class Solution:
    
    def __init__(self):
        self.current = []
        self.combs = []
        self.n = 0

    def dfs(self, candidates: List[int], i: int, total: int, target: int) -> None:
        if i >= self.n or total >= target:
            if total == target:
                self.combs.append(self.current.copy())
            return

        self.current.append(candidates[i])
        self.dfs(candidates, i, total + candidates[i], target)
        self.current.pop()
        self.dfs(candidates, i + 1, total, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)

        self.dfs(candidates, 0, 0, target)

        return self.combs

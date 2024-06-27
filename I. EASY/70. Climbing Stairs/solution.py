class Solution:
    hmap = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n not in self.hmap:
            self.hmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.hmap[n]

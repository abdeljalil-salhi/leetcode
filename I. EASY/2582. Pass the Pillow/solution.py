class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p, d = 1, 1
        for i in range(time):
            p += 1 * d
            if p == n or p == 1:
                d *= -1
        return p

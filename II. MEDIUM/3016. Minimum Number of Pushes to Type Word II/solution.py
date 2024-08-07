class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs, res = [0] * 26, 0

        for c in word:
            freqs[ord(c) - ord("a")] += 1
        freqs.sort()

        for i in range(25, -1, -1):
            if not freqs[i]:
                break
            res += freqs[i] * ((25 - i) // 8 + 1)

        return res

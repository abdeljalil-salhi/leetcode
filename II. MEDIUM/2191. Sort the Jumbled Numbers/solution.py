class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        jumbled = []

        for i, n in enumerate(nums):
            itoa = str(n)
            jumbled.append((n, int("".join(str(mapping[int(c)]) for c in itoa)), i))

        jumbled.sort(key=lambda tupl: (tupl[1], tupl[2]))

        return [tupl[0] for tupl in jumbled]

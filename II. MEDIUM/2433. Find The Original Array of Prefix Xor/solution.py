class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans, n = [pref[0]], len(pref)

        # Continuously calculate the XOR of the previous element and the current element
        for i in range(1, n):
            ans.append(pref[i] ^ pref[i - 1])

        return ans

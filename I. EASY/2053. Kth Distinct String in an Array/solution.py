class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)

        for el in hashmap:
            if hashmap[el] > 1:
                hashmap[el] = 0

        res = [el for el in hashmap if hashmap[el]]

        if len(res) < k:
            return ""

        return res[k - 1]

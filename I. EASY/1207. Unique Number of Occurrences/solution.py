class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = Counter(arr)
        visited = {}

        for el in hmap:
            if hmap[el] in visited:
                return False
            visited[hmap[el]] = 1

        return True

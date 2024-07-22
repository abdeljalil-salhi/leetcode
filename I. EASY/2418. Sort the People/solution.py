class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = [(names[i], heights[i]) for i in range(len(names))]

        pairs.sort(key=lambda pair: pair[1], reverse=True)

        return [name for name, _ in pairs]

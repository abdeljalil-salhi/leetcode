class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in descending order
        citations.sort(reverse=True)
        h = 0

        # Iterate through the sorted citations and check if the citation is greater than the index
        for i, c in enumerate(citations):
            if c >= i + 1:
                h += 1
            else:
                break  # If the citation is less than the index, break the loop

        return h

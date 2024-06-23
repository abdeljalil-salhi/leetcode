class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Yes I know this is a one-liner, but it's a one-liner that's readable
        return [i for i, w in enumerate(words) if x in w]

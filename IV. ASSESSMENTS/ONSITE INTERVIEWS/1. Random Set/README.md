# Random Set - On-site Interview #1

_Passed on June 24, 2024 6:33 PM_

![Submission](image.png)

## Unique Morse Code Words \[EASY\]

Time complexity: $O(n)$ where $n$ is the number of words

```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        def getTransformation(word: str) -> str:
            r = ""
            for c in word:
                r += morse[ord(c) - ord('a')]
            return r

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        myset = {}
        for w in words:
            myset[getTransformation(w)] = 0
        return len(myset)
```

## Peeking Iterator \[MEDIUM\]

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.peekedEl = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peekedEl = self.iterator.next()
            self.peeked = True
        return self.peekedEl

    def next(self):
        """
        :rtype: int
        """
        if not self.peeked:
            return self.iterator.next()
        result = self.peekedEl
        self.peeked = False
        self.peekedEl = None
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked or self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

## The Skyline Problem \[HARD\]

Time complexity: $O(n)$ where $n$ is the number of buildings

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        last_height = last_right = 0
        n = len(buildings)

        for i, building in enumerate(buildings):
            # if current left > previous right, the split
            if i > 0 and building[0] > buildings[i - 1][1]:
                last_height = 0
                last_right = building[1]
                points.append([buildings[i - 1][1], last_height])
                print(f"building {i} is after split")
                print([buildings[i - 1][1], last_height])

            # if fresh start, from ground to building
            if not last_height:
                if i + 1 < n and (
                    buildings[i + 1][0] == building[0]
                    and buildings[i + 1][2] > building[2]
                ):
                    continue
                last_height = building[2]  # 10
                last_right = building[1]  # 20
                points.append([building[0], last_height])
                print(f"building {i} is at fresh start, from ground up")
                print([building[0], last_height])
                continue

            # if bigger building than previouses
            if building[2] > last_height:
                if i + 1 < n and (
                    buildings[i + 1][0] == building[0]
                    and buildings[i + 1][2] > building[2]
                ):
                    continue
                last_height = building[2]
                last_right = building[1]
                points.append([building[0], last_height])
                print(f"building {i} is bigger than last height {last_height}")
                print([building[0], last_height])
            elif building[1] > last_right and building[2] < last_height:
                if i + 1 < n and (
                    buildings[i + 1][0] == building[0]
                    and buildings[i + 1][2] > building[2]
                ):
                    continue
                points.append([last_right, building[2]])
                print(
                    f"building {i} is larger than higher building, last_right={last_right}, last_height={last_height}, current_right={building[1]}"
                )
                print([last_right, building[2]])
                last_right = building[1]

        points.append([buildings[len(buildings) - 1][1], 0])
        print("ending building")
        print([buildings[n - 1][1], 0])

        return points
```

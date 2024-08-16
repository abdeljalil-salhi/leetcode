class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum, maximum, distance = arrays[0][0], arrays[0][-1], 0
        n = len(arrays)

        for i in range(1, n):
            array = arrays[i]
            distance = max(distance, abs(array[-1] - minimum), abs(array[0] - maximum))
            minimum = min(minimum, array[0])
            maximum = max(maximum, array[-1])

        return distance

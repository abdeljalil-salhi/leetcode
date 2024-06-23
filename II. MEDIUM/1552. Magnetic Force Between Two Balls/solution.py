class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def able(minimum: int) -> bool:
            count, last_position = 1, position[0]

            # Count the number of balls that can be placed with the minimum distance
            for i in range(1, n):
                if position[i] - last_position >= minimum:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True

            return False

        n = len(position)
        position.sort()
        low, high = 1, position[-1] - position[0]
        best = 0

        # Binary search for the maximum minimum distance
        while low <= high:
            mid = (low + high) // 2
            # If the minimum distance is possible, update the best distance
            if able(mid):
                best, low = mid, mid + 1
            else:
                high = mid - 1

        return best

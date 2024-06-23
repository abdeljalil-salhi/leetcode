class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def able(days: int) -> bool:
            bouquets = flowers = 0

            # Check if the flowers bloom on the given day.
            # If they do, increment the number of flowers.
            # If the number of flowers is equal to the number of flowers required to make a bouquet,
            # reset the number of flowers and increment the number of bouquets.
            # If the number of bouquets is equal to the number of bouquets required to make a bouquet,
            # return True.
            for day in bloomDay:
                if days >= day:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
                        if bouquets == m:
                            return True
                else:
                    flowers = 0

            # Return False if the number of bouquets is less than the number of bouquets required to make a bouquet.
            # (Most likely, the number of flowers is less than the number of flowers required to make a bouquet.)
            return bouquets >= m

        # If the number of bouquets required to make a bouquet is greater than the number of flowers,
        # return -1.
        n = len(bloomDay)
        if m * k > n:
            return -1

        # Binary search for the minimum number of days required to make m bouquets.
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if able(mid):
                high = mid
            else:
                low = mid + 1

        # Return the minimum number of days required to make m bouquets.
        return low

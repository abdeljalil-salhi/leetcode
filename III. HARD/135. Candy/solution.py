class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Give each child one candy
        candies = [1] * n

        # First pass: Give a candy to the right child if the rating is greater than the left child
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: Give a candy to the left child if the rating is greater than the right child
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the total number of candies
        return sum(candies)

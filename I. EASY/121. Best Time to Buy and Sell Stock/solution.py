class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit, min_price = 0, prices[0]

        for price in prices:
            # Update the minimum price if the current price is less than the minimum price
            if price < min_price:
                min_price = price
            # Update the maximum profit if the current profit is greater than the maximum profit
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

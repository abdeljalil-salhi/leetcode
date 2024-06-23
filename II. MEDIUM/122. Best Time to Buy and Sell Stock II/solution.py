class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, n, last_price = 0, len(prices), prices[0]

        # Iterate through the prices and add the profit if the price is greater than the last price
        for i in range(n):
            if last_price < prices[i]:
                profit += prices[i] - last_price
            last_price = prices[i]

        return profit

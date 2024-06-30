class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for _amount in range(amount + 1):
            for coin in coins:
                if _amount - coin >= 0:
                    dp[_amount] = min(dp[_amount], 1 + dp[_amount - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the best profit from one buy followed by one sell."""
        if not prices:
            return 0

        lowest_price = prices[0]
        best_profit = 0

        for price in prices[1:]:
            lowest_price = min(lowest_price, price)
            best_profit = max(best_profit, price - lowest_price)

        return best_profit

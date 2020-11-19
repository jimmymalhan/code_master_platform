# Buy and sell a stock twice

# Write a program that computes the maximum profit that
# can be made by buying and selling a share at most twice.
# The second buy must be on another date after the first sale.

# Hint: What do you need to know about the first i elements
# when processing the (i+1)th element?

def buy_and_sell_stock_twice(prices):
    max_profit, min_price = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we
    # sell on that day.
    for i, price in enumerate(prices):
        max_profit = max(max_profit, price -  min_price)
        min_price = min(min_price, price)
        first_buy_sell_profits[i] = max_profit
    # Backward phase. For each day, find the maximum profit if we 
    # the second buy on that day.

    max_price = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        max_profit = max(max_profit, max_profit - price + first_buy_sell_profits[i-1])
    return max_profit


# time complexity O(n)
# space complexity O(n)
# which is the space used to store the best solutions for subarrays

class Solution:
    def maxProfit(self, prices):
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2

# space complexity O(1)

# more readable 
class Solution:
    def maxProfit(self, prices):
        first_buy, second_buy, first_profit, second_profit = 1e9,1e9, 0, 0

        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price - first_buy)
            second_buy = min(second_buy, price - first_profit)
            second_profit = max(second_profit, price - second_buy)
        return second_profit
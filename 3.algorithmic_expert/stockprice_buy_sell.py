# You are given an array of Kharon stock prices, where each element is the price for the day. 
# Write a function getMaxProfit that calculates the maximum amount you can earn by buying once and 
# selling once. The worst you can do is a profit of $0 (you buy/sell even or don’t buy/sell at all).
# You can’t sell before you buy.

# Example input: [9,2,4,3,8,1,5]

# Example output: 6

class Solution:
    def __init__(self, prices):
        self.prices = prices
# O(n^2) time complexity | O(1) space complexity
    def getMaxProfit(self):
        max_profit = 0
        for i in range(len(self.prices)):
            for j in range(i+1, len(self.prices)):
                profit = self.prices[j] - self.prices[i]
                if profit > max_profit:
                    max_profit = profit # each time we find a new max profit, we update the max_profit
        return max_profit

# O(n) time complexity | O(1) space complexity
    def getMaxProfit2(self):
        max_profit = 0
        min_price = float('inf')
        for price in self.prices:
            min_price = min(min_price, price) # each time we find a new min price, we update the min_price 
            max_profit = max(max_profit, price - min_price) # each time we find a new max profit, we update the max_profit
        return max_profit

def main():
    prices = [9,2,4,3,8,1,5]
    solution = Solution(prices)
    print(solution.getMaxProfit())
    print(solution.getMaxProfit2())
    
if __name__ == '__main__':
    main()

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/Python-O(n)-by-DP-w-Visualization
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# prices = [1, 2, 3, 4, 5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.


# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float('inf'), 0 # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            cur_hold = max( prev_hold, prev_not_hold - stock_price)# either keep hold, or buy in stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )# either keep not-hold, or sell out stock today at stock price
        return cur_not_hold if prices else 0 # maximum profit must be in not-hold state

def main():
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))

main()
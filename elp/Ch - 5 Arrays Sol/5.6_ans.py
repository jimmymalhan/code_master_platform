# Write a program that takes an aray denoting daily stock price,
# and returns the maximum profit that could be made by buying and
# then selling one share of that stock. There is no need to buy if 
# no profit is possible. 

# Hint: Identifying the minimum and maximum is not enough since the
# minimum may appear after the maximum height. Focus on valid differences.

# array of the minimum values seen so far 
# maximum profit that can be made by selling on each specific day
# is the difference of the current price and minimum seen so far. 
# i.e [0,5,0,20,0,10,30,0,25,20]. hence, 30 is the maximum profit.

def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit_sell_today

# time complexity - O(n)
# space complexity - O(1)

# max method takes two or more argument or at iterable,
# For 2 arguments i.e max_profit and max_profit_sell_today,
# it returns the variable which would have maximum value

# LC = 0121.best_time_to_buy_and_sell_stock.py
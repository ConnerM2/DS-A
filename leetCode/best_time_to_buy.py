# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def sell_stonk(prices: list[int]) -> int:
    min = float("inf")
    max_profit = 0

    for price in prices:
        if price < min:
            min = price

        profit = price - min

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(sell_stonk([7,1,5,3,6,4]))
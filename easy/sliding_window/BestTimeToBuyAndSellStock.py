from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        profit = p - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

if __name__ == "__main__":
    print(maxProfit([7,6,4,3,1]))
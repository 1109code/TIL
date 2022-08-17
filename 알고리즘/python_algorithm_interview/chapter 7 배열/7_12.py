import sys
nums = [7, 1, 5, 3, 6, 4]

# sol 1 / time out
def maxProfit(prices):
    max_price = 0

    for i, price in enumerate(nums):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# sol 2
def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize
    
    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
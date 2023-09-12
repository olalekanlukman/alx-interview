#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Initialize a list with values set to a large number (greater than the maximum possible value)
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make change for amount 0
    dp[0] = 0

    # Iterate through the coins and the possible totals
    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins needed to make change for amount i
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

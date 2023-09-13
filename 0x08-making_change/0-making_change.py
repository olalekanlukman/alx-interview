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

    # Initialize the dp table with infinity except for the first element
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through the total, and for each coin, update the dp table
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

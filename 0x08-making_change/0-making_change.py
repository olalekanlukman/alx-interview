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

    # Initialize a DP array with a size of total + 1, and fill it with a value greater than the maximum possible total
    dp = [float('inf')] * (total + 1)
    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0

    # Iterate through the coins and the DP array to calculate the minimum number of coins needed for each total
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If it's not possible to make the given total, return -1
    if dp[total] == float('inf'):
        return -1
    return dp[total]


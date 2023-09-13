#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Loop through each amount from 1 to total
    for i in range(1, total + 1):
        # Loop through each coin value
        for c in coins:
            # If it is possible to make change for i - c
            if i - c >= 0 and dp[i - c] != float('inf'):
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # If total can't be made by any number of coins, return -1
    if dp[total] == float('inf'):
        return -1
    
    # Otherwise, return the minimum number of coins needed
    return dp[total]
